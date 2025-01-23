use serde::{Deserialize, Serialize};

use super::{geo_type::GeoType, symmetry::Symmetry};

/// Describes different kinds of end targets in a geometry problem.
#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug, Serialize, Deserialize)]
pub enum PredicateType {
    /// When two points are identical
    EqualPoints,
    /// When two lines are identical
    EqualLines,
    /// When two circles are identical
    EqualCircles,
    /// When three points are on a line
    Collinear,
    /// When four points are on a circle
    Concyclic,
    /// When three lines meet at a point
    Concurrent,
    /// When a point is on a line
    InLine,
    /// When a point is on a circle
    InCircle,
    /// When two circles are tangent
    TangentCircles,
    // When two segments have equal lengths
    EqualLengths,
    // When three points form a right angle
    RightAngle,
}

impl PredicateType {
    /// The parameters a Predicate using this PredicateType would require.
    pub(crate) fn signature(&self) -> Vec<GeoType> {
        match self {
            PredicateType::EqualPoints => vec![GeoType::Point, GeoType::Point],
            PredicateType::Collinear | PredicateType::RightAngle => {
                vec![GeoType::Point, GeoType::Point, GeoType::Point]
            }
            PredicateType::Concyclic | PredicateType::EqualLengths => vec![
                GeoType::Point,
                GeoType::Point,
                GeoType::Point,
                GeoType::Point,
            ],
            PredicateType::Concurrent => vec![GeoType::Line, GeoType::Line, GeoType::Line],
            PredicateType::InLine => vec![GeoType::Point, GeoType::Line],
            PredicateType::InCircle => vec![GeoType::Point, GeoType::Circle],
            PredicateType::EqualLines => vec![GeoType::Line, GeoType::Line],
            PredicateType::EqualCircles | PredicateType::TangentCircles => {
                vec![GeoType::Circle, GeoType::Circle]
            }
        }
    }

    /// The symmetries that apply in the signature of this PredicateType.
    pub(crate) fn symmetry(&self) -> Symmetry {
        match self {
            PredicateType::EqualPoints
            | PredicateType::EqualLines
            | PredicateType::EqualCircles
            | PredicateType::Collinear
            | PredicateType::Concyclic
            | PredicateType::Concurrent
            | PredicateType::TangentCircles => Symmetry::All,
            PredicateType::RightAngle => Symmetry::Reverse,
            PredicateType::InLine | PredicateType::InCircle => Symmetry::None,
            PredicateType::EqualLengths => Symmetry::TwoPairSwap,
        }
    }

    /// Formats a predicate (with given arguments) in a form that can be read by the proof generator.
    pub(crate) fn to_string(&self, arguments: &[String]) -> String {
        match self {
            PredicateType::EqualPoints
            | PredicateType::EqualLines
            | PredicateType::EqualCircles => {
                format!("{} == {}", arguments[0], arguments[1])
            }
            PredicateType::InLine | PredicateType::InCircle => {
                format!("{} in {}", arguments[0], arguments[1])
            }
            PredicateType::Collinear
            | PredicateType::Concyclic
            | PredicateType::Concurrent
            | PredicateType::TangentCircles => {
                format!("{}({})", self.name().unwrap(), arguments.join(", "))
            }
            PredicateType::EqualLengths => {
                format!(
                    "distance({}, {}) == distance({}, {})",
                    arguments[0], arguments[1], arguments[2], arguments[3]
                )
            }
            PredicateType::RightAngle => {
                format!(
                    "angle({0}, {1}, {2}) == orientation({0}, {1}, {2}) mod 360",
                    arguments[0], arguments[1], arguments[2]
                )
            }
        }
    }

    /// The name of the predicate type, to be used when formatting in `to_string`.
    /// (not all types have a name because not all types need a name when calling `to_string`)
    pub(crate) const fn name(&self) -> Option<&str> {
        Some(match self {
            PredicateType::Collinear => "collinear",
            PredicateType::Concyclic => "concyclic",
            PredicateType::Concurrent => "concurrent",
            PredicateType::TangentCircles => "tangent",
            PredicateType::EqualPoints
            | PredicateType::EqualLines
            | PredicateType::EqualCircles
            | PredicateType::InLine
            | PredicateType::InCircle
            | PredicateType::EqualLengths
            | PredicateType::RightAngle => {
                return None;
            }
        })
    }
}
