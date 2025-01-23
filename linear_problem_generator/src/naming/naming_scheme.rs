use crate::geometry::geo_type::GeoType;

/// Represents structs that can generate names for Constructions.
pub(crate) trait NamingScheme {
    /// Resets the state of the current NamingScheme.
    fn reset(&mut self);

    /// Generates a name for a new Construction.
    ///
    /// geo_type:   The type of geometry object whose name we want to generate.
    fn next_name(&mut self, geo_type: GeoType) -> String;
}
