use std::{ffi::OsString, fs, path::PathBuf};

use clap::Parser;
use glob::glob;
use tqdm::Iter;

use itertools::Itertools;
use lib::geometry::Problem;

/// The arguments that can be given to the main program.
#[derive(Parser, Default, Debug)]
struct Args {
    #[clap(
        short = 'i',
        long = "input",
        help = "Where to search for problems from.\n\
                Searches recursively inside the directory for `.json` files."
    )]
    input_dir: OsString,
    #[clap(
        short = 'o',
        long = "output",
        help = "The directory in which to save results."
    )]
    output_dir: OsString,
    #[clap(long, action, help = "Makes the program filter duplicate problems.")]
    deduplicate: bool,
    #[clap(
        long,
        action,
        help = "Will serialize problems back into `.json` files\n\
                instead of converting them to the standard `.jl` format\n\
                readable by the ProofGenerator."
    )]
    serialize: bool,
}

/// A processed version of the [`Args`] struct which is easier to work with.
#[derive(Debug)]
struct ParsedArgs {
    /// The directory in which to search for problems.
    /// (searches recursively in the directory for `.json` files)
    input_dir: PathBuf,
    /// The directory in which to save the resulting problems.
    output_dir: PathBuf,
    /// Whether the program should remove duplicate problems
    deduplicate: bool,
    /// Tells the program to serialize the resulting [`Problem`]s into `.json` files.
    /// (by default, the program will convert problems into the standard `.jl` format)
    should_serialize: bool,
}

impl TryFrom<Args> for ParsedArgs {
    type Error = anyhow::Error;

    fn try_from(args: Args) -> Result<Self, Self::Error> {
        let input_dir = PathBuf::from(&args.input_dir);
        let output_dir = PathBuf::from(&args.output_dir);

        if !input_dir.exists() {
            return Err(anyhow::format_err!(
                "ERROR: The input directory '{}' does not exist.",
                input_dir.as_os_str().to_str().unwrap()
            ));
        }

        if !output_dir.exists() {
            return Err(anyhow::format_err!(
                "ERROR: The output directory '{}' does not exist.",
                output_dir.as_os_str().to_str().unwrap()
            ));
        }

        Ok(Self {
            input_dir,
            output_dir,
            deduplicate: args.deduplicate,
            should_serialize: args.serialize,
        })
    }
}

fn main() {
    let args: ParsedArgs = Args::parse().try_into().unwrap();

    println!("Collecting problems...");
    let problems = collect_problems(&args.input_dir);
    println!("Found {} problems.", problems.len());

    let problems = if args.deduplicate {
        println!("Removing duplicate problems...");
        let deduplicated_problems = remove_duplicates(&problems);
        println!(
            "{} problems left after removing duplicates.",
            deduplicated_problems.len()
        );
        deduplicated_problems
    } else {
        problems
    };

    println!("Saving problems...");

    let file_extension = if args.should_serialize { "json" } else { "jl" };

    problems
        .iter()
        .tqdm()
        .map(|problem| problem.to_string(args.should_serialize))
        .enumerate()
        .for_each(|(problem_index, formatted_problem)| {
            let out_path = args
                .output_dir
                .join(format!("{}.{}", problem_index, file_extension));
            fs::write(out_path, formatted_problem).unwrap();
        });
}

/// Finds any `.json`-serialized problems
/// saved in `dir` (or in any of its subdirectories).
///
/// Returns the deserializes problems as a vector.
fn collect_problems(dir: &PathBuf) -> Vec<Problem> {
    let glob_pattern = dir.join("**/*.json");

    glob(glob_pattern.to_str().unwrap())
        .expect("Failed to read glob pattern")
        .filter_map(|result| match result {
            Ok(path) => Some(path),
            Err(err) => {
                println!("Glob Error: {err}");
                None
            }
        })
        .tqdm()
        .filter_map(|problem_path| {
            match serde_json::de::from_slice::<Problem>(
                &fs::read(problem_path.to_str().unwrap()).unwrap(),
            ) {
                Ok(deserialized_problem) => Some(deserialized_problem),
                Err(err) => {
                    println!("Error when deserializing: {err}");
                    None
                }
            }
        })
        .collect_vec()
}

/// Filters a list of problems so that no two are homeomorphic.
///
/// Returns the filtered problems as a vector.
fn remove_duplicates(problems: &[Problem]) -> Vec<Problem> {
    let mut result = Vec::<Problem>::new();

    for problem in problems.iter().tqdm() {
        if result
            .iter()
            .all(|other_problem| !problem.is_homeomorphic_to(&other_problem))
        {
            result.push(problem.clone());
        }
    }

    result
}
