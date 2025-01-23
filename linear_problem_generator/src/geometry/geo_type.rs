use std::{fmt::Display, hash::Hash};

use serde::{Deserialize, Serialize};

use super::predicate_type::PredicateType;

/// The different kinds of objects that can appear in a diagram.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Hash, Serialize, Deserialize)]
pub enum GeoType {
    Point,
    Line,
    Circle,
}

impl GeoType {
    pub(crate) const fn equals_predicate(&self) -> PredicateType {
        match self {
            GeoType::Point => PredicateType::EqualPoints,
            GeoType::Line => PredicateType::EqualLines,
            GeoType::Circle => PredicateType::EqualCircles,
        }
    }
}

impl Display for GeoType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            GeoType::Point => f.write_str("Point"),
            GeoType::Line => f.write_str("Line"),
            GeoType::Circle => f.write_str("Circle"),
        }
    }
}
