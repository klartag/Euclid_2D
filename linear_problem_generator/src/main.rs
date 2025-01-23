#![feature(let_chains)]

use std::{
    ffi::OsString,
    fs,
    path::{Path, PathBuf},
    process::exit,
    time::Instant,
};

use clap::Parser;
use lib::embeddings::EmbeddedDiagram;
use lib::groups::GroupAction;
use lib::problem_generation::{
    DiagramExtender, HeuristicalExtender, ProblemFinder, RepeatExtender,
    SingleRandomObjectExtender, SymmetricalExtender,
};
use tqdm::Iter;

use lib::geometry::{BaseDiagram, Diagram, PredicateType, Problem};

/// The type in which geometry problems should be embedded when searching for them.
type F = f64;

/// The arguments that can be given to the main program.
#[derive(Parser, Default, Debug)]
struct Args {
    #[clap(
        short = 'c',
        long,
        help = "The diagram to begin from when searching for problems."
    )]
    diagram: BaseDiagram,
    #[clap(
        short = 'n',
        long,
        help = "An upper limit on the number of problems to generate."
    )]
    limit: Option<usize>,
    #[clap(
        short = 'd',
        long,
        help = "The target directory in which to save problems.\n\
        (if not set, will print to stdout)"
    )]
    dir: Option<OsString>,
    #[clap(
        short,
        long,
        action,
        requires = "dir",
        help = "If the `dir` option is enabled, will save serialized problems\n\
            instead of the standard `.jl` format."
    )]
    serialize: bool,
    #[clap(
        short = 't',
        long,
        action,
        requires = "limit",
        help = "If the `limit` option is enabled, when the limit is reached,\n\
        will save a file at this path with a list of times.\n\
        The Nth value in the list is how many seconds elapsed before finding the Nth problem."
    )]
    problem_times_path: Option<OsString>,
}

/// A processed version of the [`Args`] struct which is easier to work with.
struct ParsedArgs {
    /// The target directory in which to save problems.
    /// (if not set, will print to stdout)
    dir: Option<PathBuf>,
    /// If the `dir` option is enabled, will save serialized [`Problem`]s
    /// instead of the standard `.jl` format.
    should_serialize: bool,
    /// The diagram to begin from when searching for problems
    base_diagram: Diagram,
    /// The [`GroupAction`] to use as a symmetry when extending the [`BaseDiagram`]
    group_action: Box<dyn GroupAction>,
    /// The list of vertices from [`Self::base_diagram`] which the action [`Self::group_action`] applies to.
    group_action_domain: Vec<usize>,
    /// An optional limit on the number of problems to generate
    problem_limit: Option<usize>,
    /// Where to save the list of times it took to find each problem.
    problem_times_path: Option<PathBuf>,
}

impl TryFrom<Args> for ParsedArgs {
    type Error = anyhow::Error;

    fn try_from(args: Args) -> Result<Self, Self::Error> {
        let dir: Option<&Path> = args
            .dir
            .as_deref()
            .map(|path_string| Path::new(path_string));

        let problem_times_path: Option<&Path> = args
            .problem_times_path
            .as_deref()
            .map(|path_string| Path::new(path_string));

        if let Some(out_dir) = dir
            && !out_dir.exists()
        {
            Err(anyhow::format_err!(
                "ERROR: The target directory '{}' does not exist.",
                out_dir.as_os_str().to_str().unwrap()
            ))
        } else {
            Ok(Self {
                dir: dir.map(|dir| dir.into()),
                should_serialize: args.serialize,
                base_diagram: args.diagram.diagram(),
                group_action: args.diagram.symmetries().0,
                group_action_domain: args.diagram.symmetries().1,
                problem_limit: args.limit,
                problem_times_path: problem_times_path.map(|time_out| time_out.into()),
            })
        }
    }
}

/// Runs a search using the ProblemGenerator.
fn main() {
    let args: ParsedArgs = Args::parse().try_into().unwrap();

    let mut problem_times: Vec<usize> = Default::default();

    let diagram_extender = RepeatExtender::new(
        HeuristicalExtender::new(SymmetricalExtender::new(
            SingleRandomObjectExtender::default(),
            args.group_action_domain,
            args.group_action,
        )),
        20,
    );

    let problem_finder = ProblemFinder::new(vec![
        PredicateType::Collinear,
        PredicateType::Concyclic,
        PredicateType::Concurrent,
    ]);

    let start_time = Instant::now();

    let mut found_problems: Vec<Problem> = Default::default();

    for _ in (0..).tqdm() {
        if args
            .problem_limit
            .is_some_and(|limit| found_problems.len() >= limit)
        {
            break;
        }

        let mut embedded_diagram = EmbeddedDiagram::new(args.base_diagram.clone());
        diagram_extender.extend_diagram::<F>(&mut embedded_diagram);

        let problems = problem_finder.find_problems::<F>(
            &embedded_diagram.diagram(),
            &embedded_diagram.embeddings()[0],
        );

        for problem in problems.iter() {
            if found_problems
                .iter()
                .find(|previous_problem| problem.is_homeomorphic_to(&previous_problem))
                .is_some()
            {
                continue;
            }

            let formatted_problem = problem.to_string(args.should_serialize);

            output_problem(
                found_problems.len(),
                formatted_problem,
                args.should_serialize,
                &args.dir,
            );

            found_problems.push(problem.clone());
            problem_times.push(Instant::now().duration_since(start_time).as_secs() as usize);
        }
    }

    if let Some(problem_times_path) = &args.problem_times_path {
        fs::write(
            problem_times_path,
            serde_json::ser::to_string(&problem_times).unwrap(),
        )
        .unwrap();
    }
}

fn output_problem(
    problem_index: usize,
    formatted_problem: String,
    should_serialize: bool,
    dir: &Option<PathBuf>,
) {
    if let Some(dir) = dir {
        let file_extension = if should_serialize { "json" } else { "jl" };
        let out_path = dir.join(format!("{}.{}", problem_index, file_extension));

        fs::write(out_path, formatted_problem).unwrap_or_else(|error| {
            println!(
                "Failed to write to {} due to the following error:",
                dir.as_os_str().to_str().unwrap()
            );
            println!("{:?}", error);
            exit(1);
        });
    } else {
        println!(
            "Problem #{problem_index}:\n\
                    \n\
                    {formatted_problem}\n\
                    \n"
        );
    }
}
