use std::{fmt::Display, mem};

use crate::embeddings::GeoFloat;

use super::{
    embedded_circle::EmbeddedCircle, embedded_object::EmbeddingError, embedded_point::EmbeddedPoint,
};

/// The embedding of a line
#[derive(Clone, Copy, PartialEq, Debug)]
pub struct EmbeddedLine<F: GeoFloat> {
    /// One of the points the line goes through
    pub(crate) a: EmbeddedPoint<F>,
    /// Another of the points the line goes through
    pub(crate) b: EmbeddedPoint<F>,
}

impl<F: GeoFloat + Display> Display for EmbeddedLine<F> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("Line({}, {})", self.a, self.b))
    }
}

impl<F: GeoFloat> EmbeddedLine<F> {
    pub(crate) fn new(p1: EmbeddedPoint<F>, p2: EmbeddedPoint<F>) -> EmbeddedLine<F> {
        EmbeddedLine { a: p1, b: p2 }
    }
}

impl<F: GeoFloat> EmbeddedLine<F> {
    /// Returns a unit vector in the direction of the line
    pub(crate) fn unit_direction(&self) -> EmbeddedPoint<F> {
        (self.b - self.a).normalized()
    }

    /// Returns the coefficients of the line equation, in the from `c[0]*x + c[1]*y + c[2] == 0`.
    pub(crate) fn coefficients(&self) -> [F; 3] {
        let a = self.b.y - self.a.y;
        let b = self.a.x - self.b.x;
        [a, b, -a * self.a.x - b * self.a.y]
    }

    /// Returns the unique intersection of two lines
    pub(crate) fn intersection(
        &self,
        other: EmbeddedLine<F>,
    ) -> Result<EmbeddedPoint<F>, EmbeddingError> {
        let mut self_coefs = self.coefficients();
        let mut other_coefs = other.coefficients();
        // TODO: Some lines are supposed to be parallel, but their intersection is for some reason still well defined.
        // Parallel lines do not have a well-defined intersection.
        if (self_coefs[0] * other_coefs[1] - self_coefs[1] * other_coefs[0]).is_approx_zero() {
            return Err(EmbeddingError::Illegal);
        }
        if self_coefs[0].is_approx_zero() {
            mem::swap(&mut self_coefs, &mut other_coefs);
        }

        let c = other_coefs[0] / self_coefs[0];
        other_coefs[0] = F::from_i32(0).unwrap();
        other_coefs[1] = other_coefs[1] - c * self_coefs[1];
        other_coefs[2] = other_coefs[2] - c * self_coefs[2];
        let c = self_coefs[1] / other_coefs[1];
        self_coefs[1] = F::from_i32(0).unwrap();
        self_coefs[2] = self_coefs[2] - c * other_coefs[2];

        Ok(EmbeddedPoint::new(
            -self_coefs[2] / self_coefs[0],
            -other_coefs[2] / other_coefs[1],
        ))
    }

    /// Returns intersections with a circle
    pub(crate) fn circle_intersections(
        &self,
        c: EmbeddedCircle<F>,
    ) -> Result<(EmbeddedPoint<F>, EmbeddedPoint<F>), EmbeddingError> {
        let proj = c.center.project(*self);
        let dist_sqr = proj.distance_squared(c.center);
        // The intersections of a line passing through the center of a circle and the circle are degenerate,
        // and will not be considered.
        if dist_sqr.is_approx_zero_sqr() {
            return Err(EmbeddingError::Illegal);
        }
        if !(c.radius_sqr - dist_sqr).has_sqrt() {
            return Err(EmbeddingError::Undefined);
        }
        let ortho = (c.radius_sqr - dist_sqr).sqrt();

        let diff = (proj - c.center).normalized().rotate90();
        Ok((proj + diff * ortho, proj - diff * ortho))
    }

    /// Returns the internal angle bisector where the angle is defined by three points
    pub(crate) fn internal_angle_bisector(
        p1: EmbeddedPoint<F>,
        p2: EmbeddedPoint<F>,
        p3: EmbeddedPoint<F>,
    ) -> Result<EmbeddedLine<F>, EmbeddingError> {
        let d1 = p2.distance_squared(p1);
        let d3 = p2.distance_squared(p3);
        if d1.is_approx_zero_sqr() || d3.is_approx_zero_sqr() {
            return Err(EmbeddingError::Illegal);
        }
        let norm_p3 = (p3 - p2) * (d1 / d3).sqrt() + p2;
        // This is the case where the three points are collinear.
        // I don't allow such trivial bisectors.
        if p1.distance_squared(norm_p3).is_approx_zero_sqr()
            || p2
                .distance_squared((p1 + norm_p3) / (F::one() + F::one()))
                .is_approx_zero_sqr()
        {
            return Err(EmbeddingError::Illegal);
        }

        Ok(EmbeddedLine::new(p2, p1 + norm_p3 - p2))
    }

    /// Returns the external angle bisector where the angle is defined by three points
    pub(crate) fn external_angle_bisector(
        p1: EmbeddedPoint<F>,
        p2: EmbeddedPoint<F>,
        p3: EmbeddedPoint<F>,
    ) -> Result<EmbeddedLine<F>, EmbeddingError> {
        let d1 = p2.distance_squared(p1);
        let d3 = p2.distance_squared(p3);
        if d1.is_approx_zero_sqr() || d3.is_approx_zero_sqr() {
            return Err(EmbeddingError::Illegal);
        }
        let norm_p3 = (p3 - p2) * (d1 / d3).sqrt() + p2;
        // This is the case where the three points are collinear.
        // I don't allow such trivial bisectors.
        if p1.distance_squared(norm_p3).is_approx_zero_sqr()
            || p2
                .distance_squared((p1 + norm_p3) / (F::one() + F::one()))
                .is_approx_zero_sqr()
        {
            return Err(EmbeddingError::Illegal);
        }

        Ok(EmbeddedLine::new(p2, p2 + p1 - norm_p3))
    }
}

#[cfg(test)]
mod test {
    use rand::{rngs::StdRng, Rng, SeedableRng};

    use crate::embeddings::geo_float::GeoFloat;

    use super::{EmbeddedLine, EmbeddedPoint};

    #[test]
    fn test_coefficients() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let l = EmbeddedLine::new(p1, p2);
            let coefs = l.coefficients();
            assert!(
                (coefs[0] * p1.x + coefs[1] * p1.y + coefs[2]).is_approx_zero(),
                "Line coefficients failed with err {}: {}*x + {}*y + {}, p1={:?} p2={:?}",
                coefs[0] * p1.x + coefs[1] * p1.y + coefs[2],
                coefs[0],
                coefs[1],
                coefs[2],
                p1,
                p2
            );
            assert!(
                (coefs[0] * p2.x + coefs[1] * p2.y + coefs[2]).is_approx_zero(),
                "Line coefficients failed with err {}: {}*x + {}*y + {}, p1={:?} p2={:?}",
                coefs[0] * p2.x + coefs[1] * p2.y + coefs[2],
                coefs[0],
                coefs[1],
                coefs[2],
                p1,
                p2
            );
        }
    }

    #[test]
    fn test_intersection() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p3 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p4 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let l1 = EmbeddedLine::new(p1, p2);
            let l2 = EmbeddedLine::new(p3, p4);
            let i = l1.intersection(l2).unwrap();
            assert!(i.line_distance_squared(l1).is_approx_zero_sqr());
            assert!(i.line_distance_squared(l2).is_approx_zero_sqr());
        }
    }

    #[test]
    fn test_internal_bisector() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p3 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());

            let bisector = EmbeddedLine::<f64>::internal_angle_bisector(p1, p2, p3).unwrap();

            assert!(
                ((p1 - p1.project(bisector)) / p1.distance(p2))
                    .distance_squared((p3.project(bisector) - p3) / p3.distance(p2))
                    .is_approx_zero_sqr(),
                "p1={p1:?} p2={p2:?} p3={p3:?} bisector={bisector:?}"
            )
        }
    }

    #[test]
    fn test_external_bisector() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p3 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());

            let bisector = EmbeddedLine::<f64>::external_angle_bisector(p1, p2, p3).unwrap();

            assert!(
                ((p1 - p1.project(bisector)) / p1.distance(p2))
                    .distance_squared((p3 - p3.project(bisector)) / p3.distance(p2))
                    .is_approx_zero_sqr(),
                "p1={p1:?} p2={p2:?} p3={p3:?} bisector={bisector:?}"
            )
        }
    }
}
