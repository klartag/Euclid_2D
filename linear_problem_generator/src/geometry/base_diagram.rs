use std::collections::HashMap;

use crate::groups::{
    dihedral_group::group::DihedralGroup, group_action::GroupAction,
    symmetric_group::SymmetricGroup, trivial_group::TrivialGroup,
};

use super::{construction_type::ConstructionType, diagram::Diagram};

/// The different diagrams that the Linear search can begin from.
#[derive(clap::ValueEnum, Clone, Default, Debug)]
pub enum BaseDiagram {
    /// An arbitrary triangle.
    #[default]
    Triangle,
    /// Like [`Self::Triangle`],
    /// but searches for diagrams with symmetries between two of the vertices.
    TriangleHalfSymmetric,
    /// Like [`Self::Triangle`],
    /// but searches for diagrams with symmetries between all of the vertices.
    TriangleSymmetric,
    /// A triangle, together with it's altitudes, their feet, and the orthocenter.
    Altitudes,
    /// A triangle, it's altitudes, the nine points in the nine-point-circle, and the orthocenter.
    NinePointCircle,
    /// An arbitrary quadrilateral inscribed in a circle.
    InscribedQuadrilateral,
    /// Like [`Self::InscribedQuadrilateral`],
    /// but looks for diagrams with symmetries that preserve the quadrilateral.
    InscribedQuadrilateralSymmetric,
    /// A triangle, the incircle, it's center, and it's tangent points.
    Incircle,
    /// An arbitrary parallelogram.
    Parallelogram,
    /// Like [`Self::Parallelogram`],
    /// but looks for diagrams with symmetries that preserve the parallelogram.
    ParallelogramSymmetric,
    /// An arbitrary isoceles trapezoid, and the circle it is inscribed in.
    IsocelesTrapezoid,
}

impl BaseDiagram {
    pub fn diagram(&self) -> Diagram {
        let blueprint = self.blueprint();

        let name_indices = blueprint
            .iter()
            .enumerate()
            .map(|(index, construction_blueprint)| (construction_blueprint.name.clone(), index))
            .collect::<HashMap<_, _>>();

        let mut diagram = Diagram::new();

        blueprint.iter().for_each(|construction_blueprint| {
            let arguments = construction_blueprint
                .arguments
                .iter()
                .map(|argument_name| name_indices[argument_name])
                .collect::<Vec<_>>();

            let new_construction =
                diagram.construct(construction_blueprint.construction_type, &arguments);
            diagram.push(new_construction);
        });

        diagram
    }

    fn blueprint(&self) -> Vec<ConstructionBlueprint> {
        match self {
            Self::Triangle | Self::TriangleHalfSymmetric | Self::TriangleSymmetric => triangle(),
            Self::Altitudes => altitudes(),
            Self::NinePointCircle => nine_point_circle(),
            Self::InscribedQuadrilateral | Self::InscribedQuadrilateralSymmetric => {
                inscribed_quadrilateral()
            }
            Self::Incircle => incircle(),
            Self::Parallelogram | Self::ParallelogramSymmetric => parallelogram(),
            Self::IsocelesTrapezoid => isoceles_trapezoid(),
        }
    }

    pub fn symmetries(&self) -> (Box<dyn GroupAction>, Vec<usize>) {
        match self {
            BaseDiagram::Triangle
            | BaseDiagram::Altitudes
            | BaseDiagram::NinePointCircle
            | BaseDiagram::InscribedQuadrilateral
            | BaseDiagram::Incircle
            | BaseDiagram::Parallelogram
            | BaseDiagram::IsocelesTrapezoid => (Box::new(TrivialGroup::default()), vec![]),
            BaseDiagram::TriangleHalfSymmetric => {
                (Box::new(SymmetricGroup::<2>::new()), vec![1, 2])
            }
            BaseDiagram::TriangleSymmetric => (Box::new(SymmetricGroup::<3>::new()), vec![0, 1, 2]),
            BaseDiagram::InscribedQuadrilateralSymmetric => {
                (Box::new(DihedralGroup::new(4)), vec![1, 2, 3, 4])
            }
            BaseDiagram::ParallelogramSymmetric => {
                (Box::new(DihedralGroup::new(4)), vec![0, 1, 2, 7])
            }
        }
    }
}

/// The details needed to create a single construction in a `BaseDiagram`.
struct ConstructionBlueprint {
    /// The name of the construction.
    name: String,
    /// Which type of construction should be created.
    construction_type: ConstructionType,
    /// The [`ConstructionBlueprint::name`]s of the constructions to be used as arguments in the construction.
    arguments: Vec<String>,
}

impl ConstructionBlueprint {
    fn new(name: &str, construction_type: ConstructionType, arguments: Vec<&str>) -> Self {
        Self {
            name: name.to_string(),
            construction_type,
            arguments: arguments.into_iter().map(|arg| arg.to_string()).collect(),
        }
    }
}

fn triangle() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("AC", ConstructionType::Line, vec!["A", "C"]),
    ]
}

fn altitudes() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("AC", ConstructionType::Line, vec!["A", "C"]),
        ConstructionBlueprint::new("D", ConstructionType::Projection, vec!["A", "BC"]),
        ConstructionBlueprint::new("E", ConstructionType::Projection, vec!["B", "AC"]),
        ConstructionBlueprint::new("F", ConstructionType::Projection, vec!["C", "AB"]),
        ConstructionBlueprint::new("AD", ConstructionType::Line, vec!["A", "D"]),
        ConstructionBlueprint::new("BE", ConstructionType::Line, vec!["B", "E"]),
        ConstructionBlueprint::new("CF", ConstructionType::Line, vec!["C", "F"]),
        ConstructionBlueprint::new("H", ConstructionType::LineIntersection, vec!["AD", "BE"]),
    ]
}

fn nine_point_circle() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("AC", ConstructionType::Line, vec!["A", "C"]),
        ConstructionBlueprint::new("D", ConstructionType::Projection, vec!["A", "BC"]),
        ConstructionBlueprint::new("E", ConstructionType::Projection, vec!["B", "AC"]),
        ConstructionBlueprint::new("F", ConstructionType::Projection, vec!["C", "AB"]),
        ConstructionBlueprint::new("AD", ConstructionType::Line, vec!["A", "D"]),
        ConstructionBlueprint::new("BE", ConstructionType::Line, vec!["B", "E"]),
        ConstructionBlueprint::new("CF", ConstructionType::Line, vec!["C", "F"]),
        ConstructionBlueprint::new("H", ConstructionType::LineIntersection, vec!["AD", "BE"]),
        ConstructionBlueprint::new("P", ConstructionType::Midpoint, vec!["A", "H"]),
        ConstructionBlueprint::new("Q", ConstructionType::Midpoint, vec!["B", "H"]),
        ConstructionBlueprint::new("R", ConstructionType::Midpoint, vec!["C", "H"]),
        ConstructionBlueprint::new("U", ConstructionType::Midpoint, vec!["B", "C"]),
        ConstructionBlueprint::new("V", ConstructionType::Midpoint, vec!["A", "C"]),
        ConstructionBlueprint::new("W", ConstructionType::Midpoint, vec!["A", "B"]),
    ]
}

fn inscribed_quadrilateral() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("c", ConstructionType::NewCircle, vec![]),
        ConstructionBlueprint::new("A", ConstructionType::PointOnCircle, vec!["c"]),
        ConstructionBlueprint::new("B", ConstructionType::PointOnCircle, vec!["c"]),
        ConstructionBlueprint::new("C", ConstructionType::PointOnCircle, vec!["c"]),
        ConstructionBlueprint::new("D", ConstructionType::PointOnCircle, vec!["c"]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("CD", ConstructionType::Line, vec!["C", "D"]),
        ConstructionBlueprint::new("AC", ConstructionType::Line, vec!["A", "C"]),
        ConstructionBlueprint::new("BD", ConstructionType::Line, vec!["B", "D"]),
    ]
}

fn incircle() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("AC", ConstructionType::Line, vec!["A", "C"]),
        ConstructionBlueprint::new(
            "AI",
            ConstructionType::InternalBisector,
            vec!["C", "A", "B"],
        ),
        ConstructionBlueprint::new(
            "BI",
            ConstructionType::InternalBisector,
            vec!["A", "B", "C"],
        ),
        ConstructionBlueprint::new(
            "CI",
            ConstructionType::InternalBisector,
            vec!["B", "C", "A"],
        ),
        ConstructionBlueprint::new("I", ConstructionType::LineIntersection, vec!["AI", "BI"]),
        ConstructionBlueprint::new("D", ConstructionType::Projection, vec!["I", "BC"]),
        ConstructionBlueprint::new("E", ConstructionType::Projection, vec!["I", "AC"]),
        ConstructionBlueprint::new("F", ConstructionType::Projection, vec!["I", "AB"]),
        ConstructionBlueprint::new("c", ConstructionType::Circumcircle, vec!["D", "E", "F"]),
    ]
}

fn parallelogram() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("CD", ConstructionType::Parallel, vec!["AB", "C"]),
        ConstructionBlueprint::new("DA", ConstructionType::Parallel, vec!["BC", "A"]),
        ConstructionBlueprint::new("D", ConstructionType::LineIntersection, vec!["CD", "DA"]),
    ]
}

fn isoceles_trapezoid() -> Vec<ConstructionBlueprint> {
    vec![
        ConstructionBlueprint::new("A", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("B", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("C", ConstructionType::NewPoint, vec![]),
        ConstructionBlueprint::new("AB", ConstructionType::Line, vec!["A", "B"]),
        ConstructionBlueprint::new("BC", ConstructionType::Line, vec!["B", "C"]),
        ConstructionBlueprint::new("CD", ConstructionType::Parallel, vec!["AB", "C"]),
        ConstructionBlueprint::new("c", ConstructionType::Circumcircle, vec!["A", "B", "C"]),
        ConstructionBlueprint::new(
            "D",
            ConstructionType::LineCircleOtherIntersection,
            vec!["C", "CD", "c"],
        ),
        ConstructionBlueprint::new("DA", ConstructionType::Line, vec!["A", "D"]),
    ]
}

#[cfg(test)]
mod test {
    use rstest::rstest;
    use rstest_reuse::{apply, template};

    use super::BaseDiagram;

    #[template]
    #[rstest]
    #[case(BaseDiagram::Triangle)]
    #[case(BaseDiagram::TriangleHalfSymmetric)]
    #[case(BaseDiagram::TriangleSymmetric)]
    #[case(BaseDiagram::Altitudes)]
    #[case(BaseDiagram::NinePointCircle)]
    #[case(BaseDiagram::InscribedQuadrilateral)]
    #[case(BaseDiagram::InscribedQuadrilateralSymmetric)]
    #[case(BaseDiagram::Incircle)]
    #[case(BaseDiagram::Parallelogram)]
    #[case(BaseDiagram::ParallelogramSymmetric)]
    #[case(BaseDiagram::IsocelesTrapezoid)]
    fn base_diagram_cases(#[case] base_diagram: BaseDiagram) {}

    /// Tries to build a BaseDiagram.
    /// (Tests to see if any [`ConstructionBlueprint`]s have incorrect names)
    #[apply(base_diagram_cases)]
    fn test_diagram(base_diagram: BaseDiagram) {
        base_diagram.diagram();
    }

    /// Checks whether a BaseDiagram's symmetries are compatible with its Diagram.
    #[apply(base_diagram_cases)]
    fn test_group_action_domain(base_diagram: BaseDiagram) {
        let diagram = base_diagram.diagram();
        let (group_action, domain) = base_diagram.symmetries();

        assert_eq!(
            group_action.domain_size(),
            domain.len(),
            "The domain of the group action must match the group."
        );

        let geo_types = domain
            .into_iter()
            .map(|i| diagram.constructions[i].geo_type())
            .collect::<Vec<_>>();

        for geo_type in geo_types.iter() {
            assert_eq!(
                geo_types[0], *geo_type,
                "All diagram GeoTypes in the group domain must be identical."
            );
        }
    }
}
