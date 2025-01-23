use std::fmt::Debug;

use num_traits::{Euclid, Float, FromPrimitive};

use super::tau::Tau;

/// A trait that number-like values have to implement to be able to be a field that Constructions can be embedded in.
pub trait GeoFloat:
    PartialEq + Clone + Copy + Debug + Float + FromPrimitive + Euclid + Tau
{
    /// A small value such that if two GeoFloats are this close,
    /// we consider them to be the same.
    const EPSILON: Self;

    /// The value of [`GeoFloat::EPSILON`], squared.
    const EPSILON_SQUARED: Self;

    /// Whether a square root can be taken from this value.
    fn has_sqrt(&self) -> bool {
        self.is_sign_positive()
    }

    /// Whether the value is close to zero (up to [`GeoFloat::EPSILON`])
    fn is_approx_zero(&self) -> bool {
        self.abs() < Self::EPSILON
    }

    /// Whether the value is *really* close to zero (up to [`GeoFloat::EPSILON`]^2)
    fn is_approx_zero_sqr(&self) -> bool {
        self.abs() < Self::EPSILON_SQUARED
    }
}

impl GeoFloat for f64 {
    const EPSILON: f64 = 1e-6;
    const EPSILON_SQUARED: f64 = 1e-12;
}

impl GeoFloat for f32 {
    const EPSILON: f32 = 1e-6;
    const EPSILON_SQUARED: f32 = 1e-12;
}
