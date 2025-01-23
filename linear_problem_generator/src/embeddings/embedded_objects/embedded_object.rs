use crate::{embeddings::GeoFloat, geometry::geo_type::GeoType};

use super::{
    embedded_circle::EmbeddedCircle, embedded_line::EmbeddedLine, embedded_point::EmbeddedPoint,
};

/// An enum describing geometry objects embedded in F^2
#[derive(Clone, Copy, Debug, PartialEq)]
pub enum EmbeddedObject<F: GeoFloat> {
    Point(EmbeddedPoint<F>),
    Line(EmbeddedLine<F>),
    Circle(EmbeddedCircle<F>),
}

/// An enum describing errors that happen when trying to embed objects.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub enum EmbeddingError {
    Undefined,
    Illegal,
}

impl<F: GeoFloat> EmbeddedObject<F> {
    pub(crate) const fn geo_type(&self) -> GeoType {
        match self {
            EmbeddedObject::Point(_) => GeoType::Point,
            EmbeddedObject::Line(_) => GeoType::Line,
            EmbeddedObject::Circle(_) => GeoType::Circle,
        }
    }
}

impl<F: GeoFloat> TryFrom<EmbeddedObject<F>> for EmbeddedPoint<F> {
    type Error = anyhow::Error;

    fn try_from(value: EmbeddedObject<F>) -> Result<Self, Self::Error> {
        if let EmbeddedObject::Point(p) = value {
            Ok(p)
        } else {
            Err(anyhow::format_err!(
                "Expected `EmbeddedObject::Point`, found {:?}.",
                value
            ))
        }
    }
}

impl<F: GeoFloat> TryFrom<EmbeddedObject<F>> for EmbeddedLine<F> {
    type Error = anyhow::Error;

    fn try_from(value: EmbeddedObject<F>) -> Result<Self, Self::Error> {
        if let EmbeddedObject::Line(l) = value {
            Ok(l)
        } else {
            Err(anyhow::format_err!(
                "Expected `EmbeddedObject::Line`, found {:?}.",
                value
            ))
        }
    }
}

impl<F: GeoFloat> TryFrom<EmbeddedObject<F>> for EmbeddedCircle<F> {
    type Error = anyhow::Error;

    fn try_from(value: EmbeddedObject<F>) -> Result<Self, Self::Error> {
        if let EmbeddedObject::Circle(c) = value {
            Ok(c)
        } else {
            Err(anyhow::format_err!(
                "Expected `EmbeddedObject::Circle`, found {:?}.",
                value
            ))
        }
    }
}
