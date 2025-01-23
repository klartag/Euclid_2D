use serde::{Deserialize, Serialize};
use smallvec::{smallvec, SmallVec};

use super::{geo_type::GeoType, symmetry::Symmetry};

/// Types of ways in which existing Constructions can be combined to form a new Construction.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Hash, PartialOrd, Ord, Serialize, Deserialize)]
pub enum ConstructionType {
    /// An arbitrary point
    NewPoint,
    /// An arbitrary line
    NewLine,
    /// An arbitrary circle
    NewCircle,
    /// An arbitrary point on a line
    PointOnLine,
    /// An arbitrary point on a circle
    PointOnCircle,
    /// A line defined by two points
    Line,
    /// The center of a circle
    Center,
    /// The point at which two lines intersect
    LineIntersection,
    /// A circle defined by three points
    Circumcircle,
    /// The projection of a point onto a line
    Projection,
    /// An arbitrary line through a point
    LineOnPoint,
    /// A point at which a line and circle intersect
    /// (This must be deterministically chosen out of the two possible intersections)
    LineCircleIntersection,
    /// A point at two circles intersect
    /// (This must be deterministically chosen out of the two possible intersections)
    CircleIntersection,
    /// The second point of intersection of a line and a circle
    /// (The first point of intersection is given as an argument)
    LineCircleOtherIntersection,
    /// The second point of intersection of two circles
    /// (The first point of intersection is given as an argument)
    CircleCircleOtherIntersection,
    /// A circle with a given center that goes through a given point
    CircleFromCenterAndRadius,
    /// An arbitrary circle with a given center
    CircleFromCenter,
    /// The internal bisector of an angle defined by three points
    InternalBisector,
    /// The external bisector of an angle defined by three points
    ExternalBisector,
    /// The midpoint of a line segment
    Midpoint,
    /// A line parallel to a given line through a given point
    Parallel,
    /// A tangent line from a point to a circle
    /// (This must be deterministically chosen out of the two possible tangent lines)
    Tangent,
    /// The other tangent line from a point to a circle
    /// (The first tangent line is given as an argument)
    OtherTangent,
    /// An arbitrary point collinear to two other points
    CollinearPoint,
}

impl ConstructionType {
    /// The parameters a Construction using this ConstructionType would require.
    pub(crate) fn signature(&self) -> SmallVec<[GeoType; 3]> {
        match self {
            ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle => smallvec![],

            ConstructionType::LineOnPoint | ConstructionType::CircleFromCenter => {
                smallvec![GeoType::Point]
            }
            ConstructionType::Line
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::Midpoint => smallvec![GeoType::Point, GeoType::Point],
            ConstructionType::Circumcircle
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector => {
                smallvec![GeoType::Point, GeoType::Point, GeoType::Point]
            }

            ConstructionType::PointOnLine => smallvec![GeoType::Line],
            ConstructionType::LineIntersection => smallvec![GeoType::Line, GeoType::Line],
            ConstructionType::Projection => smallvec![GeoType::Point, GeoType::Line],
            ConstructionType::Parallel => smallvec![GeoType::Line, GeoType::Point],

            ConstructionType::PointOnCircle | ConstructionType::Center => {
                smallvec![GeoType::Circle]
            }

            ConstructionType::LineCircleIntersection => smallvec![GeoType::Line, GeoType::Circle],
            ConstructionType::CircleIntersection => smallvec![GeoType::Circle, GeoType::Circle],
            ConstructionType::LineCircleOtherIntersection => {
                smallvec![GeoType::Point, GeoType::Line, GeoType::Circle]
            }
            ConstructionType::CircleCircleOtherIntersection => {
                smallvec![GeoType::Point, GeoType::Circle, GeoType::Circle]
            }

            ConstructionType::Tangent => smallvec![GeoType::Point, GeoType::Circle],
            ConstructionType::OtherTangent => {
                smallvec![GeoType::Point, GeoType::Circle, GeoType::Line]
            }
            ConstructionType::CollinearPoint => smallvec![GeoType::Point, GeoType::Point],
        }
    }

    /// The symmetries that apply in the signature of this ConstructionType.
    pub(crate) const fn symmetry(&self) -> Symmetry {
        match self {
            ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle
            | ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle
            | ConstructionType::LineCircleIntersection
            | ConstructionType::LineCircleOtherIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::Center
            | ConstructionType::Projection
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent
            | ConstructionType::Parallel
            | ConstructionType::LineOnPoint
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::CircleFromCenter => Symmetry::None,
            ConstructionType::Line
            | ConstructionType::Circumcircle
            | ConstructionType::CollinearPoint
            | ConstructionType::Midpoint
            | ConstructionType::LineIntersection => Symmetry::All,
            ConstructionType::CircleCircleOtherIntersection => Symmetry::SwapLast01,
            ConstructionType::InternalBisector | ConstructionType::ExternalBisector => {
                Symmetry::Reverse
            }
        }
    }

    /// The GeoType that this ConstructionType represents
    pub(crate) const fn geo_type(&self) -> GeoType {
        match self {
            ConstructionType::NewPoint
            | ConstructionType::Center
            | ConstructionType::LineIntersection
            | ConstructionType::PointOnCircle
            | ConstructionType::PointOnLine
            | ConstructionType::Projection
            | ConstructionType::LineCircleIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::LineCircleOtherIntersection
            | ConstructionType::CircleCircleOtherIntersection
            | ConstructionType::Midpoint
            | ConstructionType::CollinearPoint => GeoType::Point,
            ConstructionType::NewLine
            | ConstructionType::Line
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent
            | ConstructionType::Parallel
            | ConstructionType::LineOnPoint => GeoType::Line,
            ConstructionType::NewCircle
            | ConstructionType::Circumcircle
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::CircleFromCenter => GeoType::Circle,
        }
    }

    /// Returns whether a Construction using this ConstructionType is deterministic.
    /// (i.e, will always return the same Embedded object each time it is embedded)
    pub(crate) const fn is_deterministic(&self) -> bool {
        self.degrees_of_freedom() == 0
    }

    /// How many nondeterministic degrees of freedom a Construction using this ConstructionType has.
    pub(crate) const fn degrees_of_freedom(&self) -> usize {
        match *self {
            ConstructionType::Line
            | ConstructionType::Center
            | ConstructionType::LineIntersection
            | ConstructionType::Circumcircle
            | ConstructionType::Projection
            | ConstructionType::LineCircleIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::LineCircleOtherIntersection
            | ConstructionType::CircleCircleOtherIntersection
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::CircleFromCenter
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector
            | ConstructionType::Midpoint
            | ConstructionType::Parallel
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent => 0,

            ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle
            | ConstructionType::LineOnPoint
            | ConstructionType::CollinearPoint => 1,

            ConstructionType::NewPoint | ConstructionType::NewLine => 2,

            ConstructionType::NewCircle => 3,
        }
    }

    /// Formats a construction (with given arguments) in a form that can be read by the proof generator.
    pub(crate) fn to_string(&self, name: &str, arguments: &[&str]) -> Option<String> {
        match self {
            ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle => None,
            ConstructionType::PointOnLine | ConstructionType::PointOnCircle => {
                Some(format!("{} in {}", name, arguments[0]))
            }
            ConstructionType::LineOnPoint => Some(format!(
                "{} in {} # (defining {})",
                arguments[0], name, name
            )),
            ConstructionType::Line
            | ConstructionType::Center
            | ConstructionType::LineIntersection
            | ConstructionType::Circumcircle
            | ConstructionType::Projection
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector
            | ConstructionType::Midpoint => Some(format!(
                "{} == {}({})",
                name,
                self.name().unwrap(),
                arguments.join(", ")
            )),
            ConstructionType::Parallel => Some(format!(
                "{} == {}({}, {})",
                name,
                self.name().unwrap(),
                arguments[1],
                arguments[0],
            )),
            ConstructionType::CircleCircleOtherIntersection
            | ConstructionType::LineCircleOtherIntersection => {
                Some(format!("{} in {}, {}", name, arguments[1], arguments[2]))
            }
            ConstructionType::CollinearPoint => Some(format!(
                "{} in Line({}, {})",
                name, arguments[0], arguments[1]
            )),
            ConstructionType::CircleFromCenterAndRadius | ConstructionType::CircleIntersection => {
                Some(format!(
                    "{} == {:?}({}) # (WARNING: UNIMPLEMENTED IN PROOF GENERATOR)",
                    name,
                    self,
                    arguments.join(", ")
                ))
            }
            ConstructionType::LineCircleIntersection => unimplemented!(),
            ConstructionType::CircleFromCenter => unimplemented!(),
            ConstructionType::Tangent => unimplemented!(),
            ConstructionType::OtherTangent => unimplemented!(),
        }
    }

    /// The name of the ConstructionType, to be used when formatting in `to_string`.
    /// (not all types have a name because not all types need a name when calling `to_string`)
    const fn name(&self) -> Option<&str> {
        Some(match self {
            ConstructionType::Line => "Line",
            ConstructionType::Circumcircle => "Circle",
            ConstructionType::Center => "center",
            ConstructionType::LineIntersection => "line_intersection",
            ConstructionType::Projection => "projection",
            ConstructionType::InternalBisector => "internal_angle_bisector",
            ConstructionType::ExternalBisector => "external_angle_bisector",
            ConstructionType::Midpoint => "midpoint",
            ConstructionType::Parallel => "parallel_line",
            ConstructionType::LineCircleOtherIntersection => "line_circle_other_intersection",
            ConstructionType::CircleCircleOtherIntersection => "circle_circle_other_intersection",
            ConstructionType::LineCircleIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::CircleFromCenter
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent
            | ConstructionType::CollinearPoint => unimplemented!(),
            ConstructionType::LineOnPoint
            | ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle
            | ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle => {
                return None;
            }
        })
    }
}
