use std::ops::{
    Add, AddAssign, BitXor, BitXorAssign, Div, DivAssign, Index, IndexMut, Mul, MulAssign, Neg,
    Sub, SubAssign,
};

/// An implementation of a generic mathematical vector class.
#[derive(Clone, PartialEq, Debug, Default)]
pub struct Vector<T> {
    pub data: Vec<T>,
}

impl<T: Clone + Default> Vector<T> {
    pub fn new(data: Vec<T>) -> Vector<T> {
        Vector { data }
    }

    pub fn resize(&mut self, new_length: usize) {
        self.data.resize(new_length, T::default());
    }
    pub fn len(&self) -> usize {
        self.data.len()
    }
    pub fn iter(&self) -> std::slice::Iter<T> {
        self.data.iter()
    }
    pub fn iter_mut(&mut self) -> std::slice::IterMut<T> {
        self.data.iter_mut()
    }
}

impl<T> FromIterator<T> for Vector<T> {
    fn from_iter<Iter: IntoIterator<Item = T>>(iter: Iter) -> Self {
        let data = Vec::from_iter(iter);
        Vector { data }
    }
}

impl<T: Add<Output = T> + Clone> Add for &Vector<T> {
    type Output = Vector<T>;

    fn add(self, rhs: &Vector<T>) -> Vector<T> {
        self.data
            .iter()
            .zip(rhs.data.iter())
            .map(|(i, j)| i.clone() + j.clone())
            .collect()
    }
}

impl<T: BitXor<Output = T> + Clone> BitXor for &Vector<T> {
    type Output = Vector<T>;

    fn bitxor(self, rhs: &Vector<T>) -> Vector<T> {
        self.data
            .iter()
            .zip(rhs.data.iter())
            .map(|(i, j)| i.clone() ^ j.clone())
            .collect()
    }
}

impl<T: Sub<Output = T> + Clone> Sub for &Vector<T> {
    type Output = Vector<T>;

    fn sub(self, rhs: &Vector<T>) -> Vector<T> {
        self.data
            .iter()
            .zip(rhs.data.iter())
            .map(|(i, j)| i.clone() - j.clone())
            .collect()
    }
}

impl<T: Mul<Output = T> + Clone> Mul<T> for &Vector<T> {
    type Output = Vector<T>;

    fn mul(self, rhs: T) -> Vector<T> {
        self.data.iter().cloned().map(|i| i * rhs.clone()).collect()
    }
}

impl<T: Div<Output = T> + Clone> Div<T> for &Vector<T> {
    type Output = Vector<T>;

    fn div(self, rhs: T) -> Vector<T> {
        self.data.iter().cloned().map(|i| i / rhs.clone()).collect()
    }
}

impl<T: AddAssign + Clone> AddAssign<T> for Vector<T> {
    fn add_assign(&mut self, rhs: T) {
        self.data.iter_mut().for_each(|t| *t += rhs.clone())
    }
}

impl<T: BitXorAssign + Clone> BitXorAssign<T> for Vector<T> {
    fn bitxor_assign(&mut self, rhs: T) {
        self.data.iter_mut().for_each(|t| *t ^= rhs.clone())
    }
}

impl<T: SubAssign + Clone> SubAssign<T> for Vector<T> {
    fn sub_assign(&mut self, rhs: T) {
        self.data.iter_mut().for_each(|t| *t -= rhs.clone())
    }
}

impl<T: AddAssign + Clone> AddAssign<&Vector<T>> for Vector<T> {
    fn add_assign(&mut self, rhs: &Vector<T>) {
        self.data
            .iter_mut()
            .zip(rhs.data.iter())
            .for_each(|(t, u)| *t += u.clone())
    }
}
impl<T: BitXorAssign + Clone> BitXorAssign<&Vector<T>> for Vector<T> {
    fn bitxor_assign(&mut self, rhs: &Vector<T>) {
        self.data
            .iter_mut()
            .zip(rhs.data.iter())
            .for_each(|(t, u)| *t ^= u.clone())
    }
}

impl<T: SubAssign + Clone> SubAssign<&Vector<T>> for Vector<T> {
    fn sub_assign(&mut self, rhs: &Vector<T>) {
        self.data
            .iter_mut()
            .zip(rhs.data.iter())
            .for_each(|(t, u)| *t -= u.clone())
    }
}
impl<T: AddAssign> AddAssign<Vector<T>> for Vector<T> {
    fn add_assign(&mut self, rhs: Vector<T>) {
        self.data
            .iter_mut()
            .zip(rhs.data.into_iter())
            .for_each(|(t, u)| *t += u)
    }
}

impl<T: SubAssign> SubAssign<Vector<T>> for Vector<T> {
    fn sub_assign(&mut self, rhs: Vector<T>) {
        self.data
            .iter_mut()
            .zip(rhs.data.into_iter())
            .for_each(|(t, u)| *t -= u)
    }
}

impl<T: DivAssign + Clone> DivAssign<T> for Vector<T> {
    fn div_assign(&mut self, rhs: T) {
        self.data.iter_mut().for_each(|t| *t /= rhs.clone())
    }
}

impl<T: MulAssign + Clone> MulAssign<T> for Vector<T> {
    fn mul_assign(&mut self, rhs: T) {
        self.data.iter_mut().for_each(|t| *t *= rhs.clone())
    }
}

impl<T> Neg for Vector<T>
where
    T: Neg<Output = T>,
{
    type Output = Vector<T>;

    fn neg(self) -> Self::Output {
        self.data.into_iter().map(|i| -i).collect()
    }
}

// All the lifetime annotations here are a huge overkill, but I didn't want to restrict to T: Clone unnecessarily.
impl<'t, T> Neg for &Vector<T>
where
    Self: 't,
    &'t T: Neg<Output = T>,
{
    type Output = Vector<T>;

    fn neg(self) -> Self::Output {
        self.data.iter().map(|i| -i).collect()
    }
}

impl<T> Index<usize> for Vector<T> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        &self.data[index]
    }
}

impl<T> IndexMut<usize> for Vector<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        &mut self.data[index]
    }
}

// Implementing standard operations for boolean vector.
impl Add<&Vector<bool>> for Vector<bool> {
    type Output = Vector<bool>;

    fn add(self, rhs: &Vector<bool>) -> Self::Output {
        self.bitxor(rhs)
    }
}

impl Sub<&Vector<bool>> for Vector<bool> {
    type Output = Vector<bool>;

    fn sub(self, rhs: &Vector<bool>) -> Self::Output {
        self.bitxor(rhs)
    }
}
