use std::collections::HashSet;

use crate::{geometry::geo_type::GeoType, naming::naming_scheme::NamingScheme};

/// Letters that can be assigned to names of points.
const POINT_BASE_NAMES: &str = "ABCDEFGHIJKLMNOPQRSTUVWZ";

/// Letters that can be assigned to names of lines.
const LINE_BASE_NAMES: &str = "fghijklmnpqrstabcde";

/// Letters that can be assigned to names of circles.
const CIRCLE_BASE_NAMES: &str = "cdefghkpqrst";

/// A [`NamingScheme`] that hands out names in the same way that GeoGebra gives names to objects.
#[derive(Clone, Debug, Default)]
pub(crate) struct GeoGebraNaming {
    /// The names that have been generated so far.
    generated_names: HashSet<String>,
    /// The amount of point names generated so far.
    point_name_index: usize,
    /// The amount of line names generated so far.
    line_name_index: usize,
    /// The amount of circle names generated so far.
    circle_name_index: usize,
}

impl GeoGebraNaming {
    /// Generates a name according to GeoGebra naming conventions.
    ///
    /// index:      The index in the name list belonging to the
    ///             current `geo_type` that we want to generate.
    /// geo_type:   The type of object we are giving a name to.
    fn get_name(&self, index: usize, geo_type: GeoType) -> String {
        let base_names = match geo_type {
            GeoType::Point => POINT_BASE_NAMES,
            GeoType::Line => LINE_BASE_NAMES,
            GeoType::Circle => CIRCLE_BASE_NAMES,
        };

        let base_name = base_names
            .chars()
            .nth(index % base_names.len())
            .unwrap()
            .to_string();
        let count = index / base_names.len();

        match count {
            0 => base_name,
            _ => base_name + &(count - 1).to_string(),
        }
    }

    fn get_mut_name_index(&mut self, geo_type: GeoType) -> &mut usize {
        match geo_type {
            GeoType::Point => &mut self.point_name_index,
            GeoType::Line => &mut self.line_name_index,
            GeoType::Circle => &mut self.circle_name_index,
        }
    }
}

impl NamingScheme for GeoGebraNaming {
    fn next_name(&mut self, geo_type: GeoType) -> String {
        let mut name_pointer = *self.get_mut_name_index(geo_type);

        loop {
            let name = self.get_name(name_pointer, geo_type);
            name_pointer += 1;

            if !self.generated_names.contains(&name) {
                *self.get_mut_name_index(geo_type) = name_pointer;
                self.generated_names.insert(name.clone());
                return name;
            }
        }
    }

    fn reset(&mut self) {
        self.generated_names = Default::default();

        self.point_name_index = 0;
        self.line_name_index = 0;
        self.circle_name_index = 0;
    }
}
