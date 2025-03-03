use rand::Rng;
use rand_distr::{
    uniform::SampleUniform, Distribution, Exp, Exp1, Normal, StandardNormal, Uniform,
};

use crate::geometry::{construction_type::ConstructionType, predicate_type::PredicateType};

use super::{
    embedded_objects::{
        embedded_circle::EmbeddedCircle, embedded_line::EmbeddedLine, embedded_point::EmbeddedPoint,
    },
    geo_float::GeoFloat,
    tau::Tau,
    CheckApply, EmbeddingError, TryEmbed,
};

impl<F: GeoFloat + Tau + SampleUniform, Meta: Rng> TryEmbed<F, Meta> for ConstructionType
where
    StandardNormal: Distribution<F>,
    Exp1: Distribution<F>,
{
    fn try_build(
        &self,
        args: &[super::EmbeddedObject<F>],
        meta: &mut Meta,
    ) -> Result<super::EmbeddedObject<F>, EmbeddingError> {
        use super::EmbeddedObject::*;

        match (self, args) {
            (ConstructionType::Line, [Point(p1), Point(p2)]) => {
                return Ok(Line(EmbeddedLine::new(*p1, *p2)));
            }
            (ConstructionType::Center, [Circle(c)]) => {
                return Ok(Point(c.center));
            }
            (ConstructionType::LineIntersection, [Line(l1), Line(l2)]) => {
                return l1.intersection(*l2).map(|p| Point(p));
            }
            (ConstructionType::NewPoint, []) => {
                let coord_dist = Normal::new(F::zero(), F::from(10).unwrap()).unwrap();
                Ok(Point(EmbeddedPoint::new(
                    meta.sample(coord_dist),
                    meta.sample(coord_dist),
                )))
            }
            (ConstructionType::NewLine, []) => {
                let coord_dist = Normal::new(F::zero(), F::from(10).unwrap()).unwrap();
                Ok(Line(EmbeddedLine::new(
                    EmbeddedPoint::new(meta.sample(coord_dist), meta.sample(coord_dist)),
                    EmbeddedPoint::new(meta.sample(coord_dist), meta.sample(coord_dist)),
                )))
            }
            (ConstructionType::NewCircle, []) => {
                let coord_dist = Normal::new(F::zero(), F::one()).unwrap();
                let rad_dist = Exp::new(F::from_i32(3).unwrap()).unwrap();
                let res = Ok(Circle(EmbeddedCircle::new(
                    EmbeddedPoint::new(meta.sample(coord_dist), meta.sample(coord_dist)),
                    meta.sample(rad_dist),
                )));

                res
            }
            (ConstructionType::Circumcircle, [Point(p1), Point(p2), Point(p3)]) => {
                EmbeddedCircle::<F>::circumcircle(*p1, *p2, *p3).map(|c| Circle(c))
            }

            (ConstructionType::PointOnCircle, [Circle(c1)]) => {
                let angle_dist = Uniform::new(F::zero(), F::TAU);
                let angle = meta.sample(angle_dist);
                Ok(Point(
                    c1.center
                        + EmbeddedPoint::new(F::cos(angle), F::sin(angle)) * c1.radius_sqr.sqrt(),
                ))
            }
            (ConstructionType::PointOnLine, [Line(l)]) => {
                // A random point on the line is generated by picking a random point and projecting it to the line.
                let coord_dist = Normal::new(F::zero(), F::one()).unwrap();
                Ok(Point(
                    EmbeddedPoint::new(meta.sample(coord_dist), meta.sample(coord_dist))
                        .project(*l),
                ))
            }
            (ConstructionType::LineOnPoint, [Point(p)]) => {
                // A random point on the line is generated by picking a random point and projecting it to the line.
                let coord_dist = Normal::new(F::zero(), F::one()).unwrap();
                Ok(Line(EmbeddedLine::new(
                    p.clone(),
                    EmbeddedPoint::new(meta.sample(coord_dist), meta.sample(coord_dist)),
                )))
            }
            (ConstructionType::Projection, [Point(p), Line(l)]) => Ok(Point(p.project(*l))),
            (ConstructionType::LineCircleIntersection, [Line(l), Circle(c)]) => {
                // If the line passes through the center of the circle, we cannot differentiate between
                // the two intersection points without further information (Such as the line being a directed line),
                // and the construction is illegal.
                if PredicateType::InLine.applies(&[Point(c.center.clone()), Line(l.clone())]) {
                    return Err(EmbeddingError::Illegal);
                }
                let (p1, p2) = l.circle_intersections(*c)?;
                if (p1 - c.center).det(p2 - c.center).has_sqrt() {
                    Ok(Point(p1))
                } else {
                    Ok(Point(p2))
                }
            }
            (ConstructionType::LineCircleOtherIntersection, [Point(p), Line(l), Circle(c)]) => {
                let (p1, p2) = l.circle_intersections(*c)?;
                if p1.distance_squared(p2).is_approx_zero_sqr() {
                    Err(EmbeddingError::Illegal)
                } else if p.distance_squared(p1).is_approx_zero_sqr() {
                    Ok(Point(p2))
                } else if p.distance_squared(p2).is_approx_zero_sqr() {
                    Ok(Point(p1))
                } else {
                    // The given point must identically be one of the intersection points.
                    Err(EmbeddingError::Illegal)
                }
            }
            (ConstructionType::CircleIntersection, [Circle(c1), Circle(c2)]) => {
                let (p1, p2) = c1.intersections(*c2)?;
                if (c2.center - c1.center).det(p1 - c1.center).has_sqrt() {
                    Ok(Point(p1))
                } else {
                    Ok(Point(p2))
                }
            }
            (
                ConstructionType::CircleCircleOtherIntersection,
                [Point(p), Circle(c1), Circle(c2)],
            ) => {
                let Ok((p1, p2)) = c1.intersections(*c2) else {
                    return Err(EmbeddingError::Undefined);
                };

                if p1.distance_squared(p2).is_approx_zero_sqr() {
                    Err(EmbeddingError::Illegal)
                } else if p.distance_squared(p1).is_approx_zero_sqr() {
                    Ok(Point(p2))
                } else if p.distance_squared(p2).is_approx_zero_sqr() {
                    Ok(Point(p1))
                } else {
                    Err(EmbeddingError::Illegal)
                }
            }
            (ConstructionType::CircleFromCenterAndRadius, [Point(center), Point(p)]) => Ok(Circle(
                EmbeddedCircle::new(*center, center.distance_squared(*p)),
            )),
            (ConstructionType::CircleFromCenter, [Point(center)]) => {
                let rad_dist = Exp::new(F::from_i32(3).unwrap()).unwrap();

                let radius = meta.sample(rad_dist);
                Ok(Circle(EmbeddedCircle::new(*center, radius)))
            }
            (ConstructionType::Midpoint, [Point(p1), Point(p2)]) => {
                Ok(Point((*p1 + *p2) / F::from_i64(2).unwrap()))
            }
            (ConstructionType::CollinearPoint, [Point(p1), Point(p2)]) => {
                let normal = Normal::new(F::zero(), F::from_usize(4).unwrap()).unwrap();
                let ratio = meta.sample(normal);
                Ok(Point(
                    (*p1 * ratio + *p2 * (F::one() - ratio)) / F::from_i64(2).unwrap(),
                ))
            }
            (ConstructionType::InternalBisector, [Point(p1), Point(p2), Point(p3)]) => {
                EmbeddedLine::<F>::internal_angle_bisector(*p1, *p2, *p3).map(|line| Line(line))
            }
            (ConstructionType::ExternalBisector, [Point(p1), Point(p2), Point(p3)]) => {
                EmbeddedLine::<F>::external_angle_bisector(*p1, *p2, *p3).map(|line| Line(line))
            }
            (ConstructionType::Tangent, [Point(p), Circle(c)]) => {
                if (p.distance_squared(c.center) - c.radius_sqr).is_approx_zero() {
                    // The interesting tangents construction can only be used when the point is not on the line.
                    // Otherwise, it is an alias for a boring construction.
                    return Err(EmbeddingError::Illegal);
                }
                let (p1, p2) = p.tangent_points(*c)?;
                if (p1 - c.center).det(p1 - *p).has_sqrt() {
                    Ok(Line(EmbeddedLine::new(*p, p1)))
                } else {
                    Ok(Line(EmbeddedLine::new(*p, p2)))
                }
            }
            (ConstructionType::OtherTangent, [Point(p), Circle(c), Line(o)]) => {
                if (p.distance_squared(c.center) - c.radius_sqr).is_approx_zero() {
                    // The interesting tangents construction can only be used when the point is not on the line.
                    // Otherwise, it is an alias for a boring construction.
                    return Err(EmbeddingError::Illegal);
                }
                let (p1, p2) = p.tangent_points(*c)?;
                if p1.line_distance_squared(*o).is_approx_zero_sqr() {
                    Ok(Line(EmbeddedLine::new(*p, p2)))
                } else if p2.line_distance_squared(*o).is_approx_zero_sqr() {
                    Ok(Line(EmbeddedLine::new(*p, p1)))
                } else {
                    Err(EmbeddingError::Illegal)
                }
            }
            (ConstructionType::Parallel, [Line(l), Point(p)]) => {
                Ok(Line(EmbeddedLine::new(*p, l.b + *p - l.a)))
            }

            _ => panic!("Cannot construct {self:?} with args {args:?}",),
        }
    }
}
