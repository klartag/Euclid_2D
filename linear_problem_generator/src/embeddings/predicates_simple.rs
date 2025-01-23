use std::{cmp::Ordering, collections::HashSet};

use core::convert::TryInto;

use itertools::Itertools;
use rustc_hash::FxHashMap;
use smallvec::{smallvec, SmallVec};

use crate::{
    consts::MAX_ARGS,
    geometry::{diagram::Diagram, geo_type::GeoType, predicate_type::PredicateType},
};

use super::{
    embedded_objects::{
        embedded_circle::EmbeddedCircle, embedded_line::EmbeddedLine, embedded_point::EmbeddedPoint,
    },
    geo_float::GeoFloat,
    CheckApply, EmbeddedObject, Embedding,
};

/// Hashes a GeoFloat in a way that is stable under small changes
/// (i.e, with a resolution of [`GeoFloat::EPSILON`])
pub(crate) fn hash_float<F: GeoFloat>(f: F) -> Option<i64> {
    (f / F::EPSILON).to_i64()
}

/// Hashes an EmbeddedPoint<F> in a way that is stable under small changes
/// (i.e, with a resolution of [`GeoFloat::EPSILON`] in each coordinate)
pub(crate) fn hash_point<F: GeoFloat>(p: EmbeddedPoint<F>) -> Option<(i64, i64)> {
    Some((hash_float(p.x)?, hash_float(p.y)?))
}

/// Hashes an EmbeddedLine<F> in a way that is stable under small changes
/// (i.e, with a resolution of [`GeoFloat::EPSILON`] for the ratios between
/// coefficients in [`EmbeddedLine<F>::coefficients`] with the median coefficient)
pub(crate) fn hash_line<F: GeoFloat>(l: EmbeddedLine<F>) -> Option<(i64, i64, i64)> {
    let coefs = l.coefficients();
    let median = if (coefs[0] < coefs[1]) ^ (coefs[0] < coefs[2]) {
        coefs[0]
    } else if (coefs[1] < coefs[2]) ^ (coefs[1] < coefs[0]) {
        coefs[1]
    } else {
        coefs[2]
    };

    Some((
        hash_float(coefs[0] / median)?,
        hash_float(coefs[1] / median)?,
        hash_float(coefs[2] / median)?,
    ))
}

/// Hashes an EmbeddedPoint<F> in a way that is stable under small changes
/// (i.e, with a resolution of [`GeoFloat::EPSILON`] in the center coordinates
/// and the square of the radius)
pub(crate) fn hash_circle<F: GeoFloat>(c: EmbeddedCircle<F>) -> Option<((i64, i64), i64)> {
    let Some(point_hash) = hash_point(c.center) else {
        return None;
    };
    let Some(r) = hash_float(c.radius_sqr) else {
        return None;
    };
    Some((point_hash, r))
}

impl<F: GeoFloat> CheckApply<F> for PredicateType {
    fn applies(&self, args: &[EmbeddedObject<F>]) -> bool {
        use super::EmbeddedObject::*;
        match (self, args) {
            (PredicateType::EqualPoints, &[Point(p1), Point(p2)]) => {
                p1.distance_squared(p2).is_approx_zero_sqr()
            }
            (PredicateType::Collinear, &[Point(p1), Point(p2), Point(p3)]) => {
                ((p2 - p1).det(p3 - p1)).is_approx_zero()
            }
            (PredicateType::Concyclic, &[Point(p1), Point(p2), Point(p3), Point(p4)]) => {
                // The points are not concyclic if we fail to build a shared circle.
                let Ok(c) = EmbeddedCircle::<F>::circumcircle(p1, p2, p3) else {
                    return false;
                };
                c.power_of_point(p4).is_approx_zero()
            }
            (PredicateType::Concurrent, &[Line(l1), Line(l2), Line(l3)]) => {
                let Ok(p) = l1.intersection(l2) else {
                    return false;
                };
                p.line_distance_squared(l3).is_approx_zero_sqr()
            }
            (PredicateType::InLine, &[Point(p), Line(l)]) => {
                p.line_distance_squared(l).is_approx_zero_sqr()
            }
            (PredicateType::InCircle, &[Point(p), Circle(c)]) => {
                c.power_of_point(p).is_approx_zero()
            }

            (PredicateType::EqualLines, &[Line(l1), Line(l2)]) => {
                (l1.a.line_distance_squared(l2).is_approx_zero_sqr())
                    && (l1.b.line_distance_squared(l2).is_approx_zero_sqr())
            }
            (PredicateType::EqualCircles, &[Circle(c1), Circle(c2)]) => {
                c1.center.distance_squared(c2.center).is_approx_zero_sqr()
                    && (c1.radius_sqr - c2.radius_sqr).is_approx_zero()
            }
            (PredicateType::TangentCircles, &[Circle(c1), Circle(c2)]) => {
                let d1 = c1.center.distance(c2.center);
                let d2 = c1.radius_sqr.sqrt();
                let d3 = c2.radius_sqr.sqrt();

                return !d1.is_approx_zero_sqr()
                    && ((d1 - d2 - d3).is_approx_zero()
                        || (d2 - d1 - d3).is_approx_zero()
                        || (d3 - d1 - d2).is_approx_zero());
            }
            (PredicateType::EqualLengths, &[Point(p0), Point(p1), Point(p2), Point(p3)]) => {
                (p0.distance_squared(p1) - p2.distance_squared(p3)).is_approx_zero_sqr()
            }
            (PredicateType::RightAngle, &[Point(p0), Point(p1), Point(p2)]) => {
                let u = p0 - p1;
                let v = p2 - p1;
                u.dot(&v).is_approx_zero_sqr() && !u.is_approx_zero() && !v.is_approx_zero()
            }
            _ => {
                panic!("PredicateType::applies is not implemented for {self:?} {args:?}",)
            }
        }
    }

    /// Finds all k-tuples of constructions in a diagram satisfying the given predicate.
    fn find_all(
        &self,
        diagram: &Diagram,
        embedding: &Embedding<F>,
    ) -> Vec<SmallVec<[usize; MAX_ARGS]>> {
        match self {
            &PredicateType::EqualPoints => {
                let mut map = FxHashMap::default();
                for (index, obj) in embedding.iter().enumerate() {
                    let EmbeddedObject::Point(p) = obj else {
                        continue;
                    };
                    let Some(point_hash) = hash_point(*p) else {
                        continue;
                    };
                    map.entry(point_hash).or_insert(Vec::new()).push(index);
                }

                let mut res = Vec::new();
                for equal_points in map.into_values() {
                    for i in 1..equal_points.len() {
                        // Note: When there are n equal points, we output only n-1 predicates and not (n choose 2).
                        res.push(smallvec![
                            equal_points[i - 1].clone(),
                            equal_points[i].clone()
                        ]);
                    }
                }
                res
            }

            &PredicateType::EqualLines => {
                let mut map = FxHashMap::default();
                for (index, obj) in embedding.iter().enumerate() {
                    let EmbeddedObject::Line(l) = obj else {
                        continue;
                    };
                    let Some(line_hash) = hash_line(*l) else {
                        continue;
                    };
                    map.entry(line_hash).or_insert(Vec::new()).push(index);
                }

                let mut res = Vec::new();
                for equal_lines in map.into_values() {
                    for i in 1..equal_lines.len() {
                        res.push(smallvec![
                            equal_lines[i - 1].clone(),
                            equal_lines[i].clone()
                        ]);
                    }
                }
                res
            }

            &PredicateType::EqualCircles => {
                let mut map = FxHashMap::default();
                for (index, obj) in embedding.iter().enumerate() {
                    let EmbeddedObject::Circle(c) = obj else {
                        continue;
                    };
                    let Some(circle_hash) = hash_circle(*c) else {
                        continue;
                    };
                    map.entry(circle_hash).or_insert(Vec::new()).push(index);
                }

                let mut res = Vec::new();
                for equal_circles in map.into_values() {
                    for i in 1..equal_circles.len() {
                        res.push(smallvec![
                            equal_circles[i - 1].clone(),
                            equal_circles[i].clone()
                        ]);
                    }
                }
                res
            }
            &PredicateType::Collinear => {
                // Finds triples (p1, p2, p3) of collinear points in O(n^2 log(n)) time.
                // When there are tons of points on the same line, I output only triples of the form (P_0, P_i, P_{i+1}) to save time.
                // Is less efficient that the EqualPoint search, since it check O(T) possible theorems in O(T^(2/3)) time instead of O(T^(1/2)).

                let mut point_indices = diagram
                    .geo_type_to_indices
                    .get(&GeoType::Point)
                    .map(|x| x.clone())
                    .unwrap_or_else(|| vec![]);

                let mut res = Vec::new();

                while let Some(point_index) = point_indices.pop() {
                    let point =
                        TryInto::<EmbeddedPoint<F>>::try_into(embedding[point_index]).unwrap();
                    point_indices.sort_unstable_by(|&i, &j| {
                        let p1 = TryInto::<EmbeddedPoint<F>>::try_into(embedding[i]).unwrap();
                        let p2 = TryInto::<EmbeddedPoint<F>>::try_into(embedding[j]).unwrap();
                        F::partial_cmp(&(p1 - point).angle(), &(p2 - point).angle())
                            .unwrap_or(Ordering::Greater)
                    });
                    for i in 1..point_indices.len() {
                        if PredicateType::Collinear.applies(&[
                            embedding[point_index],
                            embedding[point_indices[i - 1]],
                            embedding[point_indices[i]],
                        ]) {
                            res.push(smallvec![
                                point_index,
                                point_indices[i - 1],
                                point_indices[i]
                            ]);
                        }
                    }
                }

                res
            }
            &PredicateType::EqualLengths => {
                let point_indices = diagram
                    .geo_type_to_indices
                    .get(&GeoType::Point)
                    .map(|x| x.clone())
                    .unwrap_or_else(|| vec![]);

                let mut map = FxHashMap::default();

                for index_pair in point_indices.iter().combinations(2) {
                    let i0 = *index_pair[0];
                    let i1 = *index_pair[1];
                    let p0 = TryInto::<EmbeddedPoint<F>>::try_into(embedding[i0]).unwrap();
                    let p1 = TryInto::<EmbeddedPoint<F>>::try_into(embedding[i1]).unwrap();

                    let Some(distance_hash) = hash_float(p0.distance_squared(p1)) else {
                        continue;
                    };

                    map.entry(distance_hash)
                        .or_insert(Vec::new())
                        .push((i0, i1));
                }

                map.into_iter()
                    .map(|(_, pairs)| {
                        pairs.into_iter().combinations(2).map(|quadruplets| {
                            smallvec![
                                quadruplets[0].0,
                                quadruplets[0].1,
                                quadruplets[1].0,
                                quadruplets[1].1,
                            ]
                        })
                    })
                    .flatten()
                    .collect_vec()
            }
            _ => self
                .signature()
                .iter()
                .map(|geo_type| {
                    diagram
                        .geo_type_to_indices
                        .get(geo_type)
                        .into_iter()
                        .flatten()
                        .collect::<Vec<_>>()
                })
                .multi_cartesian_product()
                .filter(|signature_instance| {
                    signature_instance.iter().collect::<HashSet<_>>().len()
                        == signature_instance.len()
                })
                .filter(|signature_instance| self.symmetry().is_minimal(&signature_instance))
                .filter(|arguments| {
                    self.applies(
                        &arguments
                            .iter()
                            .map(|argument| embedding[**argument])
                            .collect::<Vec<_>>(),
                    )
                })
                .map(|arguments| arguments.into_iter().copied().collect::<SmallVec<_>>())
                .collect::<Vec<SmallVec<_>>>(),
        }
    }
}
