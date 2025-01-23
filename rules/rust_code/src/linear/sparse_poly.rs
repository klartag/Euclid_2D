use std::{
    fmt::{Debug, Display},
    iter::Sum,
    ops::{
        Add, AddAssign, BitXor, BitXorAssign, Div, DivAssign, Index, Mul, MulAssign, Neg, Sub,
        SubAssign,
    },
};

use itertools::Itertools;
use smallvec::SmallVec;

#[derive(Clone, PartialEq, Eq, Debug, Hash)]
pub struct Monomial<Key: Ord + Clone + Copy + Debug> {
    /// A vector holding tuples of (variable name, degree).
    pub vars: SmallVec<[Key; 2]>,
}

impl<Key: Ord + Clone + Clone + Copy + Debug> Monomial<Key> {
    pub fn new(degrees: impl IntoIterator<Item = Key>) -> Monomial<Key> {
        let mut res_degrees = SmallVec::new();
        res_degrees.extend(degrees.into_iter().sorted());

        Monomial { vars: res_degrees }
    }

    /// Computes the total degree of the monomial.
    pub fn degree(&self) -> usize {
        self.vars.len()
    }

    /// Checks if the monomial is divisible by the other monomial.
    pub fn is_divisible_by(&self, other: &Monomial<Key>) -> bool {
        let mut other_idx = 0;
        let mut self_idx = 0;
        while self_idx < self.vars.len() && other_idx < other.vars.len() {
            match self.vars[self_idx].cmp(&other.vars[other_idx]) {
                std::cmp::Ordering::Less => {
                    self_idx += 1;
                }
                std::cmp::Ordering::Equal => {
                    self_idx += 1;
                    other_idx += 1;
                }
                std::cmp::Ordering::Greater => {
                    return false;
                }
            }
        }
        other_idx == other.vars.len()
    }

    /// Returns the constant monomial.
    pub fn constant() -> Monomial<Key> {
        Monomial {
            vars: SmallVec::new(),
        }
    }
}

impl<Key: Ord + Clone + Clone + Copy + Debug> PartialOrd for Monomial<Key> {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some((self.degree(), &self.vars).cmp(&(other.degree(), &other.vars)))
    }
}

impl<Key: Ord + Clone + Clone + Copy + Debug> Ord for Monomial<Key> {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl<Key: Ord + Clone + Clone + Copy + Debug> Mul for Monomial<Key> {
    type Output = Monomial<Key>;

    fn mul(self, rhs: Self) -> Self::Output {
        Monomial::new(self.vars.iter().cloned().chain(rhs.vars.iter().cloned()))
    }
}
impl<Key: Ord + Clone + Clone + Copy + Debug> Mul for &Monomial<Key> {
    type Output = Monomial<Key>;

    fn mul(self, rhs: Self) -> Self::Output {
        Monomial::new(self.vars.iter().cloned().chain(rhs.vars.iter().cloned()))
    }
}

impl<Key: Ord + Clone + Clone + Copy + Debug> Div for &Monomial<Key> {
    type Output = Option<Monomial<Key>>;

    fn div(self, rhs: Self) -> Self::Output {
        let mut res = SmallVec::with_capacity(self.degree() - rhs.degree());
        let mut rhs_idx = 0;
        for &i in &self.vars {
            if rhs_idx < rhs.vars.len() && i == rhs.vars[rhs_idx] {
                rhs_idx += 1;
            } else {
                res.push(i);
            }
        }

        if rhs_idx == rhs.degree() {
            Some(Monomial { vars: res })
        } else {
            None
        }
    }
}

impl<Key: Ord + Clone + Clone + Copy + Debug + Display> Display for Monomial<Key> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if self.degree() == 0 {
            return Ok(());
        }

        let mut acc = 0;
        let mut prev = None;
        for &v in &self.vars {
            if Some(v) == prev {
                acc += 1;
            } else {
                match acc {
                    0 => {}
                    1 => f.write_str(&format!("[{}]*", prev.unwrap()))?,
                    _ => f.write_str(&format!("[{}]^{}*", prev.unwrap(), acc))?,
                };
                acc = 1;
                prev = Some(v);
            }
        }
        if let Some(v) = prev {
            if acc == 1 {
                f.write_str(&format!("[{v}]"))?;
            } else {
                f.write_str(&format!("[{v}]^{acc}"))?;
            }
        }

        Ok(())
    }
}

/// An implementation of a generic multivariate polynomial.
#[derive(Clone, PartialEq, Debug, Default)]
pub struct MPoly<M: Copy + Ord + Debug, T: MPolyType> {
    pub data: Vec<(Monomial<M>, T)>,
}

impl<M: Copy + Ord + Debug, T: MPolyType + Clone> MPoly<M, T> {
    pub fn new(data: Vec<(Monomial<M>, T)>) -> MPoly<M, T> {
        if data.iter().all(|(_, v)| !v.is_zero())
            && data
                .iter()
                .zip(data.iter().skip(1))
                .all(|((m1, _), (m2, _))| m1 < m2)
        {
            // If the monomials in the data are unique, sorted, and contain no zeroes, we just use them.
            // This happens in most artihmetic operations.
            MPoly { data }
        } else {
            // Otherwise, we sort and dedup the monomials.
            data.into_iter().collect()
        }
    }

    pub fn len(&self) -> usize {
        self.data.len()
    }
    pub fn iter(&self) -> std::slice::Iter<(Monomial<M>, T)> {
        self.data.iter()
    }
    pub fn iter_mut(&mut self) -> std::slice::IterMut<(Monomial<M>, T)> {
        self.data.iter_mut()
    }

    /// Returns the coefficient of the given monomial.
    pub fn coefficient(&self, mon: &Monomial<M>) -> Option<&T> {
        self.data
            .binary_search_by(|(m, _)| m.cmp(&mon))
            .ok()
            .map(|idx| &self.data[idx].1)
    }

    /// Returns the coefficient of the given monomial.
    pub fn coefficient_mut(&mut self, mon: Monomial<M>) -> Option<&mut T> {
        self.data
            .binary_search_by(|(m, _)| m.cmp(&mon))
            .ok()
            .map(|idx| &mut self.data[idx].1)
    }

    /// Returns the largest pair of (Monomial, coefficient) with monomial smaller than the given monomial.
    pub fn next_largest_item(&self, mon: Monomial<M>) -> Option<&(Monomial<M>, T)> {
        if self.is_zero() || self.data[0].0 >= mon {
            return None;
        }
        let mut low = 0;
        let mut high = self.len();
        while low + 1 < high {
            let mid = (low + high) / 2;
            if self.data[mid].0 < mon {
                low = mid;
            } else {
                high = mid;
            }
        }
        Some(&self.data[low])
    }

    /// The degree of the polynomial.
    pub fn degree(&self) -> usize {
        self.data.last().map(|m| m.0.degree()).unwrap_or(0)
    }

    pub fn zero() -> MPoly<M, T> {
        MPoly::new(Vec::new())
    }

    pub fn is_zero(&self) -> bool {
        self.data.len() == 0
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Clone> MPoly<M, T> {
    pub fn constant_value(&self) -> T {
        if let Some((mon, v)) = self.data.first() {
            if mon.degree() == 0 {
                return v.clone();
            }
        }
        return T::zero().clone();
    }
    pub fn top_monomial(&self) -> (Monomial<M>, T) {
        self.data
            .last()
            .map(|t| t.clone())
            .unwrap_or((Monomial::constant(), T::zero().clone()))
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Clone> FromIterator<(Monomial<M>, T)> for MPoly<M, T> {
    fn from_iter<Iter: IntoIterator<Item = (Monomial<M>, T)>>(iter: Iter) -> Self {
        let mut data: Vec<(Monomial<M>, T)> = Vec::new();
        for (m, t) in iter
            .into_iter()
            .sorted_by(|m1, m2| m1.0.cmp(&m2.0))
            .filter(|(_, t)| !t.is_zero())
        {
            if let Some(last) = data.last_mut() {
                if last.0 == m {
                    last.1 = last.1.clone().mpoly_add(t);
                    if last.1.is_zero() {
                        data.pop();
                    }
                    continue;
                }
            }
            data.push((m, t));
        }
        MPoly { data }
    }
}

fn merge_with_fn<M: Copy + Ord + Debug, T: MPolyType + Clone>(
    v1: &[(Monomial<M>, T)],
    v2: &[(Monomial<M>, T)],
    f: impl Fn(&T, &T) -> T,
) -> Vec<(Monomial<M>, T)> {
    let mut res = Vec::with_capacity(v1.len() + v2.len());

    let mut i1 = 0;
    let mut i2 = 0;
    while i1 < v1.len() && i2 < v2.len() {
        match v1[i1].0.cmp(&v2[i2].0) {
            std::cmp::Ordering::Less => {
                res.push(v1[i1].clone());
                i1 += 1
            }
            std::cmp::Ordering::Equal => {
                res.push((v1[i1].0.clone(), f(&v1[i1].1, &v2[i2].1)));
                i1 += 1;
                i2 += 1;
            }
            std::cmp::Ordering::Greater => {
                res.push(v2[i2].clone());
                i2 += 1
            }
        }
    }

    res
}

pub trait MPolyType: 'static {
    fn is_zero(&self) -> bool;
    fn is_one(&self) -> bool;
    fn zero() -> &'static Self;
    fn mpoly_add(self, other: Self) -> Self;
    fn mpoly_sub(self, other: Self) -> Self;
}

impl MPolyType for i64 {
    fn is_zero(&self) -> bool {
        *self == 0
    }

    fn zero() -> &'static Self {
        const ZERO: i64 = 0;
        &ZERO
    }

    fn mpoly_add(self, other: Self) -> Self {
        self + other
    }

    fn mpoly_sub(self, other: Self) -> Self {
        self - other
    }

    fn is_one(&self) -> bool {
        *self == 1
    }
}

impl MPolyType for f64 {
    fn is_zero(&self) -> bool {
        self.abs() < 1e-9
    }

    fn zero() -> &'static Self {
        const ZERO: f64 = 0.;
        &ZERO
    }

    fn mpoly_add(self, other: Self) -> Self {
        self + other
    }

    fn mpoly_sub(self, other: Self) -> Self {
        self - other
    }

    fn is_one(&self) -> bool {
        MPolyType::is_zero(&(self - 1.))
    }
}

impl MPolyType for bool {
    fn is_zero(&self) -> bool {
        !self
    }

    fn zero() -> &'static Self {
        const ZERO: bool = false;
        &ZERO
    }

    fn mpoly_add(self, other: Self) -> Self {
        self ^ other
    }

    fn mpoly_sub(self, other: Self) -> Self {
        self ^ other
    }

    fn is_one(&self) -> bool {
        *self
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Add<Output = T> + Clone> Add for &MPoly<M, T> {
    type Output = MPoly<M, T>;

    fn add(self, rhs: &MPoly<M, T>) -> MPoly<M, T> {
        MPoly::new(merge_with_fn(&self.data, &rhs.data, |t1, t2| {
            t1.clone() + t2.clone()
        }))
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + BitXor<Output = T> + Clone> BitXor for &MPoly<M, T> {
    type Output = MPoly<M, T>;

    fn bitxor(self, rhs: &MPoly<M, T>) -> MPoly<M, T> {
        MPoly::new(merge_with_fn(&self.data, &rhs.data, |t1, t2| {
            t1.clone() ^ t2.clone()
        }))
    }
}

impl<
        M: Copy + Ord + Debug,
        T: MPolyType + Neg<Output = T> + Add<Output = T> + Clone + MPolyType,
    > Neg for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn neg(self) -> Self::Output {
        self.data
            .iter()
            .map(|(m, t)| (m.clone(), -t.clone()))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Neg<Output = T> + Add<Output = T> + Clone> Sub
    for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn sub(self, rhs: &MPoly<M, T>) -> MPoly<M, T> {
        self + &(-rhs)
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Mul<Output = T> + Add<Output = T> + Clone> Mul<T>
    for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn mul(self, rhs: T) -> MPoly<M, T> {
        self.data
            .iter()
            .cloned()
            .map(|(m, i)| (m.clone(), i * rhs.clone()))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Div<Output = T> + Add<Output = T> + Clone> Div<T>
    for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn div(self, rhs: T) -> MPoly<M, T> {
        self.data
            .iter()
            .cloned()
            .map(|(m, i)| (m.clone(), i / rhs.clone()))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Add<Output = T> + Clone> AddAssign<&MPoly<M, T>>
    for MPoly<M, T>
{
    fn add_assign(&mut self, rhs: &MPoly<M, T>) {
        *self = &*self + rhs
    }
}
impl<M: Copy + Ord + Debug, T: MPolyType + BitXor<Output = T> + Clone> BitXorAssign<&MPoly<M, T>>
    for MPoly<M, T>
{
    fn bitxor_assign(&mut self, rhs: &MPoly<M, T>) {
        *self = &*self ^ rhs
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Neg<Output = T> + Add<Output = T> + Clone>
    SubAssign<&MPoly<M, T>> for MPoly<M, T>
{
    fn sub_assign(&mut self, rhs: &MPoly<M, T>) {
        *self = &*self - rhs
    }
}
impl<M: Copy + Ord + Debug, T: MPolyType + Add<Output = T> + Clone> AddAssign<MPoly<M, T>>
    for MPoly<M, T>
{
    fn add_assign(&mut self, rhs: MPoly<M, T>) {
        *self = &*self + &rhs
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Neg<Output = T> + Add<Output = T> + Clone>
    SubAssign<MPoly<M, T>> for MPoly<M, T>
{
    fn sub_assign(&mut self, rhs: MPoly<M, T>) {
        *self = &*self - &rhs
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + DivAssign + Clone> DivAssign<T> for MPoly<M, T> {
    fn div_assign(&mut self, rhs: T) {
        for (_, v) in self.iter_mut() {
            *v /= rhs.clone();
        }
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + MulAssign + Clone> MulAssign<T> for MPoly<M, T> {
    fn mul_assign(&mut self, rhs: T) {
        for (_, v) in self.iter_mut() {
            *v *= rhs.clone();
        }
    }
}

impl<M: Copy + Ord + Debug, T: MPolyType + Clone> Index<Monomial<M>> for MPoly<M, T> {
    type Output = T;

    fn index(&self, index: Monomial<M>) -> &Self::Output {
        self.coefficient(&index).unwrap_or(&T::zero())
    }
}
impl<M: Copy + Ord + Debug, T: MPolyType + Clone> Index<&Monomial<M>> for MPoly<M, T> {
    type Output = T;

    fn index(&self, index: &Monomial<M>) -> &Self::Output {
        self.coefficient(index).unwrap_or(&T::zero())
    }
}

impl<M: Copy + Ord + Debug + Display, T: MPolyType + Clone + Display> Display for MPoly<M, T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let mut first = true;
        for (m, v) in &self.data {
            if !first {
                f.write_str(" + ")?;
            } else {
                first = false;
            }
            if m.degree() == 0 {
                Display::fmt(v, f)?;
            } else if v.is_one() {
                Display::fmt(m, f)?;
            } else {
                f.write_str(&format!("{v}*{m}"))?;
            }
        }
        Ok(())
    }
}

impl<
        M: Copy + Ord + Debug + Display,
        T: MPolyType + Clone + Display + Mul<Output = T> + Add<Output = T>,
    > Sum for MPoly<M, T>
{
    fn sum<I: Iterator<Item = Self>>(mut iter: I) -> Self {
        let Some(mut first) = iter.next() else {
            return MPoly::zero();
        };
        for other in iter {
            first += other;
        }
        first
    }
}
impl<M: Copy + Ord + Debug + Display, T: MPolyType + Clone + Display> Mul<Monomial<M>>
    for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn mul(self, rhs: Monomial<M>) -> Self::Output {
        self.data
            .iter()
            .map(|(m, t)| (m * &rhs, t.clone()))
            .collect()
    }
}

impl<
        M: Copy + Ord + Debug + Display,
        T: MPolyType + Clone + Display + Mul<Output = T> + Add<Output = T>,
    > Mul<&(Monomial<M>, T)> for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn mul(self, rhs: &(Monomial<M>, T)) -> Self::Output {
        self.data
            .iter()
            .map(|(m, t)| (m * &rhs.0, t.clone() * rhs.1.clone()))
            .collect()
    }
}

impl<
        M: Copy + Ord + Debug + Display,
        T: MPolyType + Clone + Display + Mul<Output = T> + Add<Output = T>,
    > Mul<&MPoly<M, T>> for &MPoly<M, T>
{
    type Output = MPoly<M, T>;

    fn mul(self, rhs: &MPoly<M, T>) -> Self::Output {
        rhs.data.iter().map(|mon| self * mon).sum()
    }
}
// Implementing standard operations for boolean vector.
impl<M: Copy + Ord + Debug> Add<&MPoly<M, bool>> for MPoly<M, bool> {
    type Output = MPoly<M, bool>;

    fn add(self, rhs: &MPoly<M, bool>) -> Self::Output {
        self.bitxor(rhs)
    }
}

impl<M: Copy + Ord + Debug> Sub<&MPoly<M, bool>> for MPoly<M, bool> {
    type Output = MPoly<M, bool>;

    fn sub(self, rhs: &MPoly<M, bool>) -> Self::Output {
        self.bitxor(rhs)
    }
}

#[cfg(test)]
mod tests {
    use super::{MPoly, Monomial};

    #[test]
    fn test_add() {
        let p1 = MPoly::new(vec![
            (Monomial::new([0, 0].into_iter()), 1),
            (Monomial::new([0, 1].into_iter()), 1),
        ]);
        let p2 = MPoly::new(vec![
            (Monomial::new([0].into_iter()), 1),
            (Monomial::new([0, 1].into_iter()), 1),
        ]);
        let p3 = MPoly::new(vec![
            (Monomial::new([0].into_iter()), 1),
            (Monomial::new([0, 0].into_iter()), 1),
            (Monomial::new([0, 1].into_iter()), 2),
        ]);

        assert_eq!(&p1 + &p2, p3)
    }
    #[test]
    fn test_sub() {
        let p1 = MPoly::new(vec![
            (Monomial::new([0, 0].into_iter()), 1),
            (Monomial::new([0, 1].into_iter()), 1),
        ]);
        let p2 = MPoly::new(vec![
            (Monomial::new([0].into_iter()), 1),
            (Monomial::new([0, 1].into_iter()), 1),
        ]);
        let p3 = MPoly::new(vec![
            (Monomial::new([0].into_iter()), -1),
            (Monomial::new([0, 0].into_iter()), 1),
        ]);

        assert_eq!(&p1 - &p2, p3)
    }
}
