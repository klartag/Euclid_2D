use std::{
    fmt::Display,
    ops::{Add, Div, Mul, Sub},
};

use crate::embeddings::GeoFloat;

use super::{
    embedded_circle::EmbeddedCircle, embedded_line::EmbeddedLine, embedded_object::EmbeddingError,
};

/// The embedding of a point
#[derive(Clone, Copy, PartialEq, Debug)]
pub struct EmbeddedPoint<F: GeoFloat> {
    /// The X coordinate of the point
    pub(crate) x: F,
    /// The Y coordinate of the point
    pub(crate) y: F,
}

impl<F: GeoFloat + Display> Display for EmbeddedPoint<F> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("({}, {})", self.x, self.y))
    }
}

impl<F: GeoFloat> EmbeddedPoint<F> {
    pub(crate) fn new(x: F, y: F) -> EmbeddedPoint<F> {
        EmbeddedPoint { x, y }
    }

    pub(crate) fn is_approx_zero(&self) -> bool {
        self.x.is_approx_zero() && self.y.is_approx_zero()
    }
}

impl<F: GeoFloat> EmbeddedPoint<F> {
    /// Returns the square of the length of a point
    pub(crate) fn length_squared(&self) -> F {
        self.dot(self)
    }

    /// Returns a point in the same direction, of length one
    pub(crate) fn normalized(&self) -> EmbeddedPoint<F> {
        *self / self.length_squared().sqrt()
    }

    /// Returns the dot product with another point
    pub(crate) fn dot(&self, other: &EmbeddedPoint<F>) -> F {
        self.x * other.x + self.y * other.y
    }

    /// Returns the length of a point
    pub(crate) fn length(&self) -> F {
        self.length_squared().sqrt()
    }

    /// Returns the projection of the point to a line
    pub(crate) fn project(&self, line: EmbeddedLine<F>) -> EmbeddedPoint<F> {
        let proj = line.unit_direction();
        line.a + proj * (*self - line.a).dot(&(line.b - line.a).normalized())
    }

    /// Returns the point rotated counter-clockwise by 90 degrees.
    pub(crate) fn rotate90(&self) -> EmbeddedPoint<F> {
        EmbeddedPoint::new(-self.y, self.x)
    }

    /// Returns the perpendicular bisector of two points
    pub(crate) fn perpendicular_bisector(
        p1: EmbeddedPoint<F>,
        p2: EmbeddedPoint<F>,
    ) -> Result<EmbeddedLine<F>, EmbeddingError> {
        if p1 == p2 {
            return Err(EmbeddingError::Illegal);
        }
        let mid = (p1 + p2) / F::from_i64(2).unwrap();
        let perp = mid + (p2 - p1).rotate90();
        Ok(EmbeddedLine::new(mid, perp))
    }

    /// Returns the square of the distance between two points
    pub(crate) fn distance_squared(self, other: EmbeddedPoint<F>) -> F {
        (self - other).length_squared()
    }

    /// Computes the distance between two points
    pub(crate) fn distance(self, other: EmbeddedPoint<F>) -> F {
        self.distance_squared(other).sqrt()
    }

    /// Returns the square of the distance from the point to a line
    pub(crate) fn line_distance_squared(self, other: EmbeddedLine<F>) -> F {
        self.distance_squared(self.project(other))
    }

    /// Returns the determinant the point has with another point,
    /// when placed in a 2x2 matrix.
    pub(crate) fn det(self, other: EmbeddedPoint<F>) -> F {
        self.x * other.y - self.y * other.x
    }

    /// Returns the points of tangency of lines going through the point,
    /// and tangent to a circle
    pub(crate) fn tangent_points(
        self,
        circle: EmbeddedCircle<F>,
    ) -> Result<(EmbeddedPoint<F>, EmbeddedPoint<F>), EmbeddingError> {
        let radius_sqr = self.distance_squared(circle.center) - circle.radius_sqr;
        if radius_sqr.has_sqrt() {
            EmbeddedCircle::new(self, radius_sqr).intersections(circle)
        } else {
            Err(EmbeddingError::Undefined)
        }
    }

    /// Returns the angle between the X-axis and the point.
    /// The angle is returned in the range `(-pi, pi]`.
    pub(crate) fn angle(&self) -> F {
        self.y.atan2(self.x)
    }
}

impl<F: GeoFloat + Add<F, Output = F>> Add for EmbeddedPoint<F> {
    type Output = EmbeddedPoint<F>;
    fn add(self, other: EmbeddedPoint<F>) -> EmbeddedPoint<F> {
        EmbeddedPoint::new(self.x + other.x, self.y + other.y)
    }
}

impl<F: GeoFloat + Sub<F, Output = F>> Sub for EmbeddedPoint<F> {
    type Output = EmbeddedPoint<F>;
    fn sub(self, other: EmbeddedPoint<F>) -> EmbeddedPoint<F> {
        EmbeddedPoint::new(self.x - other.x, self.y - other.y)
    }
}

impl<F: GeoFloat + Mul<F, Output = F>> Mul<F> for EmbeddedPoint<F> {
    type Output = EmbeddedPoint<F>;
    fn mul(self, other: F) -> EmbeddedPoint<F> {
        EmbeddedPoint::new(self.x * other.clone(), self.y * other)
    }
}

impl<F: GeoFloat + Div<F, Output = F>> Div<F> for EmbeddedPoint<F> {
    type Output = EmbeddedPoint<F>;
    fn div(self, other: F) -> EmbeddedPoint<F> {
        EmbeddedPoint::new(self.x / other.clone(), self.y / other)
    }
}

#[cfg(test)]
mod test {
    use rand::{rngs::StdRng, Rng, SeedableRng};

    use crate::embeddings::{
        embedded_objects::embedded_point::EmbeddedCircle, geo_float::GeoFloat,
    };

    use super::{EmbeddedLine, EmbeddedPoint};

    #[test]
    fn test_projection() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p3 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let l = EmbeddedLine::new(p1, p2);
            let proj = p3.project(l);
            assert!(proj.line_distance_squared(l).is_approx_zero_sqr());
            assert!(
                (p1 - proj).dot(&(p3 - proj)).is_approx_zero(),
                "Not orthogonal: {}",
                (p1 - proj).dot(&(p3 - proj))
            );
        }
    }

    #[test]
    fn test_rotate90() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let p1 = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let p2 = p1.rotate90();
            assert!(p1.dot(&p2).is_approx_zero());
        }
    }

    #[test]
    fn test_tangent() {
        let mut rng = StdRng::seed_from_u64(0x12345678);
        let mut success = 0;
        for _ in 0..100 {
            let p = EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>());
            let circ = EmbeddedCircle::new(
                EmbeddedPoint::new(rng.gen::<f64>(), rng.gen::<f64>()),
                rng.gen::<f64>(),
            );

            let Ok(tangents) = p.tangent_points(circ) else {
                continue;
            };
            success += 1;
            assert!(
                (tangents.0.distance_squared(circ.center) - circ.radius_sqr).is_approx_zero(),
                "p = {:?}, circ = {:?}, tangent = {:?}",
                p,
                circ,
                tangents.0
            );
            assert!((tangents.1.distance_squared(circ.center) - circ.radius_sqr).is_approx_zero());
            assert!((tangents.0 - p)
                .dot(&(tangents.0 - circ.center))
                .is_approx_zero());
            assert!((tangents.1 - p)
                .dot(&(tangents.1 - circ.center))
                .is_approx_zero());
        }
        assert!(success > 10);
    }
}
