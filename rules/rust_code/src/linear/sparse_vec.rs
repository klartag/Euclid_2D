use std::{
    fmt::{Debug, Display, Write},
    iter::Sum,
    ops::{Add, AddAssign, Div, DivAssign, Mul, MulAssign, Neg, Sub, SubAssign},
};

use itertools::Itertools;

/// An implementation of a sparse vector.
#[derive(Clone, PartialEq, Debug, Default)]
pub struct SparseVector<M: Copy + Ord + Debug, T: SparseVecType> {
    pub data: Vec<(M, T)>,
}

impl<M: Copy + Ord + Debug, T: SparseVecType> SparseVector<M, T> {
    pub fn new(data: Vec<(M, T)>) -> SparseVector<M, T> {
        if data.iter().all(|(_, v)| !v.is_zero())
            && data
                .iter()
                .zip(data.iter().skip(1))
                .all(|((m1, _), (m2, _))| m1 < m2)
        {
            // If the monomials in the data are unique, sorted, and contain no zeroes, we just use them.
            // This happens in most artihmetic operations.
            SparseVector { data }
        } else {
            // Otherwise, we sort and dedup the monomials.
            data.into_iter().collect()
        }
    }

    pub fn len(&self) -> usize {
        self.data.len()
    }
    pub fn iter(&self) -> std::slice::Iter<(M, T)> {
        self.data.iter()
    }
    pub fn iter_mut(&mut self) -> std::slice::IterMut<(M, T)> {
        self.data.iter_mut()
    }

    /// Returns the coefficient of the given monomial.
    pub fn coefficient(&self, mon: &M) -> Option<&T> {
        self.data
            .binary_search_by(|(m, _)| m.cmp(&mon))
            .ok()
            .map(|idx| &self.data[idx].1)
    }

    /// Returns the coefficient of the given monomial.
    pub fn coefficient_mut(&mut self, mon: M) -> Option<&mut T> {
        self.data
            .binary_search_by(|(m, _)| m.cmp(&mon))
            .ok()
            .map(|idx| &mut self.data[idx].1)
    }

    /// Returns the largest pair of (Monomial, coefficient) with monomial smaller than the given monomial.
    pub fn next_largest_item(&self, mon: M) -> Option<&(M, T)> {
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

    pub fn zero() -> SparseVector<M, T> {
        SparseVector::new(Vec::new())
    }

    pub fn is_zero(&self) -> bool {
        self.data.len() == 0
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType> SparseVector<M, T> {
    pub fn top_item(&self) -> Option<&(M, T)> {
        self.data.last()
    }
    pub fn top_coefficient(&self) -> Option<T> {
        self.data.last().map(|t| t.1.clone())
    }
    pub fn top_monomial(&self) -> Option<M> {
        self.data.last().map(|t| t.0.clone())
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType> FromIterator<(M, T)> for SparseVector<M, T> {
    fn from_iter<Iter: IntoIterator<Item = (M, T)>>(iter: Iter) -> Self {
        let mut data: Vec<(M, T)> = Vec::new();
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
        SparseVector { data }
    }
}

fn merge_with_fn<M: Copy + Ord + Debug, T: SparseVecType>(
    v1: &[(M, T)],
    v2: &[(M, T)],
    f: impl Fn(&T, &T) -> T,
) -> Vec<(M, T)> {
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
    res.extend(v1[i1..].iter().cloned());
    res.extend(v2[i2..].iter().cloned());

    res
}

pub trait SparseVecType: 'static + Clone {
    fn zero() -> Self;
    fn is_zero(&self) -> bool;
    fn one() -> Self;
    fn is_one(&self) -> bool;
    fn mpoly_add(&self, other: Self) -> Self;
    fn mpoly_sub(&self, other: Self) -> Self;
    fn mpoly_mul(&self, other: Self) -> Self;
    fn mpoly_neg(&self) -> Self;
}

impl SparseVecType for i64 {
    fn is_zero(&self) -> bool {
        *self == 0
    }

    fn zero() -> Self {
        0
    }

    fn mpoly_add(&self, other: Self) -> Self {
        self + other
    }

    fn mpoly_sub(&self, other: Self) -> Self {
        self - other
    }

    fn is_one(&self) -> bool {
        *self == 1
    }

    fn one() -> Self {
        1
    }

    fn mpoly_mul(&self, other: Self) -> Self {
        self * other
    }

    fn mpoly_neg(&self) -> Self {
        -self
    }
}
impl SparseVecType for i32 {
    fn is_zero(&self) -> bool {
        *self == 0
    }

    fn zero() -> Self {
        0
    }

    fn mpoly_add(&self, other: Self) -> Self {
        self + other
    }

    fn mpoly_sub(&self, other: Self) -> Self {
        self - other
    }

    fn is_one(&self) -> bool {
        *self == 1
    }

    fn one() -> Self {
        1
    }

    fn mpoly_mul(&self, other: Self) -> Self {
        self * other
    }

    fn mpoly_neg(&self) -> Self {
        -self
    }
}

impl SparseVecType for f64 {
    fn is_zero(&self) -> bool {
        self.abs() < 1e-9
    }

    fn zero() -> Self {
        0.
    }

    fn mpoly_add(&self, other: Self) -> Self {
        self + other
    }

    fn mpoly_sub(&self, other: Self) -> Self {
        self - other
    }

    fn is_one(&self) -> bool {
        SparseVecType::is_zero(&(self - 1.))
    }

    fn one() -> Self {
        1.
    }

    fn mpoly_mul(&self, other: Self) -> Self {
        self * other
    }

    fn mpoly_neg(&self) -> Self {
        -self
    }
}

impl SparseVecType for bool {
    fn is_zero(&self) -> bool {
        !self
    }

    fn zero() -> Self {
        false
    }

    fn mpoly_add(&self, other: Self) -> Self {
        self ^ other
    }

    fn mpoly_sub(&self, other: Self) -> Self {
        self ^ other
    }

    fn is_one(&self) -> bool {
        *self
    }

    fn one() -> Self {
        true
    }

    fn mpoly_mul(&self, other: Self) -> Self {
        self & other
    }

    fn mpoly_neg(&self) -> Self {
        *self
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> Add for &SparseVector<M, T> {
    type Output = SparseVector<M, T>;

    fn add(self, rhs: &SparseVector<M, T>) -> SparseVector<M, T> {
        SparseVector::new(merge_with_fn(&self.data, &rhs.data, |t1, t2| {
            t1.clone().mpoly_add(t2.clone())
        }))
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone + SparseVecType> Neg for &SparseVector<M, T> {
    type Output = SparseVector<M, T>;

    fn neg(self) -> Self::Output {
        self.data
            .iter()
            .map(|(m, t)| (m.clone(), t.mpoly_neg()))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> Sub for &SparseVector<M, T> {
    type Output = SparseVector<M, T>;

    fn sub(self, rhs: &SparseVector<M, T>) -> SparseVector<M, T> {
        self + &(-rhs)
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> Mul<T> for &SparseVector<M, T> {
    type Output = SparseVector<M, T>;

    fn mul(self, rhs: T) -> SparseVector<M, T> {
        self.data
            .iter()
            .cloned()
            .map(|(m, i)| (m.clone(), i.mpoly_mul(rhs.clone())))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Div<Output = T>> Div<T> for &SparseVector<M, T> {
    type Output = SparseVector<M, T>;

    fn div(self, rhs: T) -> SparseVector<M, T> {
        self.data
            .iter()
            .cloned()
            .map(|(m, i)| (m.clone(), i / rhs.clone()))
            .collect()
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> AddAssign<&SparseVector<M, T>>
    for SparseVector<M, T>
{
    fn add_assign(&mut self, rhs: &SparseVector<M, T>) {
        *self = &*self + rhs
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> SubAssign<&SparseVector<M, T>>
    for SparseVector<M, T>
{
    fn sub_assign(&mut self, rhs: &SparseVector<M, T>) {
        *self = &*self - rhs
    }
}
impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> AddAssign<SparseVector<M, T>>
    for SparseVector<M, T>
{
    fn add_assign(&mut self, rhs: SparseVector<M, T>) {
        *self = &*self + &rhs
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + Clone> SubAssign<SparseVector<M, T>>
    for SparseVector<M, T>
{
    fn sub_assign(&mut self, rhs: SparseVector<M, T>) {
        *self = &*self - &rhs
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + DivAssign + Clone> DivAssign<T>
    for SparseVector<M, T>
{
    fn div_assign(&mut self, rhs: T) {
        for (_, v) in self.iter_mut() {
            *v /= rhs.clone();
        }
    }
}

impl<M: Copy + Ord + Debug, T: SparseVecType + MulAssign + Clone> MulAssign<T>
    for SparseVector<M, T>
{
    fn mul_assign(&mut self, rhs: T) {
        for (_, v) in self.iter_mut() {
            *v *= rhs.clone();
        }
    }
}

impl<M: Copy + Ord + Debug + Display, T: SparseVecType + Display> Display for SparseVector<M, T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if self.len() == 0 {
            return f.write_char('0');
        }
        let mut first = true;
        for (m, v) in &self.data {
            if !first {
                f.write_str(" + ")?;
            } else {
                first = false;
            }
            if v.is_one() {
                f.write_char('[')?;
                Display::fmt(m, f)?;
                f.write_char(']')?;
            } else {
                f.write_str(&format!("{v}*[{m}]"))?;
            }
        }
        Ok(())
    }
}

impl<M: Copy + Ord + Debug + Display, T: SparseVecType + Display + Mul<Output = T>> Sum
    for SparseVector<M, T>
{
    fn sum<I: Iterator<Item = Self>>(mut iter: I) -> Self {
        let Some(mut first) = iter.next() else {
            return SparseVector::zero();
        };
        for other in iter {
            first += other;
        }
        first
    }
}

#[cfg(test)]
mod tests {
    use super::SparseVector;

    #[test]
    fn test_add() {
        let p1 = SparseVector::new(vec![(0, 1), (1, 1)]);
        let p2 = SparseVector::new(vec![(2, 1), (1, 1)]);
        let p3 = SparseVector::new(vec![(2, 1), (0, 1), (1, 2)]);

        assert_eq!(&p1 + &p2, p3)
    }
    #[test]
    fn test_sub() {
        let p1 = SparseVector::new(vec![(2, 1), (1, 1)]);
        let p2 = SparseVector::new(vec![(2, 1), (1, 1)]);
        let p3 = SparseVector::new(vec![(2, -1), (2, 1)]);

        assert_eq!(&p1 - &p2, p3);

        let p1 = SparseVector::new(vec![(0, 1)]);
        let p2 = SparseVector::new(vec![]);
        assert_eq!(&p1 - &p2, p1);
    }
}
