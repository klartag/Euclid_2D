use std::fmt::Display;

use num_traits::Float;

use crate::embeddings::GeoFloat;

use super::{embedded_object::EmbeddingError, embedded_point::EmbeddedPoint};

/// The embedding of a circle
#[derive(Clone, Copy, PartialEq, Debug)]
pub struct EmbeddedCircle<F: GeoFloat> {
    /// The center of the circle
    pub(crate) center: EmbeddedPoint<F>,
    /// The square of the radius of the circle
    pub(crate) radius_sqr: F,
}

impl<F: GeoFloat + Display + Float> Display for EmbeddedCircle<F> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!(
            "Circle({}, {})",
            self.center,
            self.radius_sqr.abs().sqrt()
        ))
    }
}

impl<F: GeoFloat> EmbeddedCircle<F> {
    pub(crate) fn new(center: EmbeddedPoint<F>, radius_sqr: F) -> EmbeddedCircle<F> {
        EmbeddedCircle { center, radius_sqr }
    }
}

impl<F: GeoFloat> EmbeddedCircle<F> {
    /// Returns the power of a point with respect to this circle
    pub(crate) fn power_of_point(&self, p: EmbeddedPoint<F>) -> F {
        p.distance_squared(self.center) - self.radius_sqr
    }

    /// Returns a unique circle passing through three points
    pub(crate) fn circumcircle(
        p1: EmbeddedPoint<F>,
        p2: EmbeddedPoint<F>,
        p3: EmbeddedPoint<F>,
    ) -> Result<EmbeddedCircle<F>, EmbeddingError> {
        let Ok(l1) = EmbeddedPoint::<F>::perpendicular_bisector(p1, p2) else {
            return Err(EmbeddingError::Illegal);
        };
        let Ok(l2) = EmbeddedPoint::<F>::perpendicular_bisector(p1, p3) else {
            return Err(EmbeddingError::Illegal);
        };
        let Ok(center) = l1.intersection(l2) else {
            return Err(EmbeddingError::Illegal);
        };
        Ok(EmbeddedCircle::new(center, center.distance_squared(p1)))
    }

    /// Returns the circle's intersections with another circle
    pub(crate) fn intersections(
        &self,
        c2: EmbeddedCircle<F>,
    ) -> Result<(EmbeddedPoint<F>, EmbeddedPoint<F>), EmbeddingError> {
        let diff = c2.center - self.center;
        let d = diff.length();
        // if d + F::EPSILON > self.radius + c2.radius {
        //     return Err(EmbFail::Undefined);
        // }
        // if c2.radius + F::EPSILON > self.radius + d {
        //     return Err(EmbFail::Undefined);
        // }
        // if self.radius + F::EPSILON > c2.radius + d {
        //     return Err(EmbFail::Undefined);
        // }

        let a_minus_b = (self.radius_sqr - c2.radius_sqr) / d;
        let a = (a_minus_b + d) / F::from_f32(2.).unwrap();
        let h = (self.radius_sqr - a * a).sqrt();
        if h.is_nan() {
            return Err(EmbeddingError::Undefined);
        }
        let diff = diff.normalized();
        Ok((
            self.center + diff * a + diff.rotate90() * h,
            self.center + diff * a - diff.rotate90() * h,
        ))
    }
}

#[cfg(test)]
mod test {
    use rand::{rngs::StdRng, Rng, SeedableRng};

    use crate::embeddings::{geo_float::GeoFloat, tau::Tau};

    use super::{EmbeddedCircle, EmbeddedPoint};

    #[test]
    fn test_circumcircle() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let center = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let radius = rng.gen::<f64>();
            let radius_sqr = radius.powi(2);
            let angle_1 = rng.gen::<f64>() * f64::TAU;
            let angle_2 = rng.gen::<f64>() * f64::TAU;
            let angle_3 = rng.gen::<f64>() * f64::TAU;
            let p2 = center + EmbeddedPoint::new(radius * angle_2.cos(), radius * angle_2.sin());
            let p1 = center + EmbeddedPoint::new(radius * angle_1.cos(), radius * angle_1.sin());
            let p3 = center + EmbeddedPoint::new(radius * angle_3.cos(), radius * angle_3.sin());

            let c2 = EmbeddedCircle::<f64>::circumcircle(p1, p2, p3).unwrap();
            assert!(c2.center.distance_squared(center).is_approx_zero_sqr());
            assert!((c2.radius_sqr - radius_sqr).is_approx_zero());
        }
    }

    #[test]
    fn test_circle_intersection() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let r1 = rng.gen::<f64>();
            let r2 = (p1.distance(p2)) - r1 + 1.;
            let c1 = EmbeddedCircle::new(p1, r1);
            let c2 = EmbeddedCircle::new(p2, r2);
            if let Ok((i1, i2)) = c1.intersections(c2) {
                assert!(c1.power_of_point(i1).is_approx_zero());
                assert!(c2.power_of_point(i1).is_approx_zero());
                assert!(c1.power_of_point(i2).is_approx_zero());
                assert!(c2.power_of_point(i2).is_approx_zero());
            }
        }
    }
}
