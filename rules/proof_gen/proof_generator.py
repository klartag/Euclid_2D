from dataclasses import dataclass
from enum import Enum
import glob
import os
from pathlib import Path
import pickle
import random
import heapq
import multiprocessing
import hashlib
import time
from glob import glob
from typing import Callable, Optional

from frozendict import frozendict

from rules.embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPrediateCollector

from ..trimmers.old_trimmer import max_depth_trim

from ..interactive_predicate_checker import InteractivePredicateChecker


from ..predicates.predicate import Predicate
from ..predicates.global_predicates import get_constructions
from ..predicates.predicate_factory import predicate_from_args
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.construction_object import Construction, ConstructionObject
from ..embeddings.embedded_predicate_value import EmbeddedPredicateValue
from ..proof import CommentStep, ObjDefineStep, Proof, Step, TheoremStep
from ..proof_checker import CHECK_CFG, TRUST_NO_ADD_CFG, ProofChecker, involved_objects
from ..proof_checker_utils import KNOWN_KEYS
from .gen_utils import is_trivial
from .scores import StepSuggestion, get_result_predicates
from ..signature_dag import IntersectPattern, SignatureDag
from ..rule_utils import LITERAL, GeometryError, IllegalObjectError, ProofCheckError
from ..theorem import Theorem
from util import BASE_PATH


class ProofGeneratorErrorType(Enum):
    NoMoreSteps = ('There were no more steps to run',)
    Timeout = 'The proof generator reached its timeout'
    Contradiction = 'A contradiction was found'
    StepLimitReached = 'Reached the limited amount of steps the generator is allowed to run'


@dataclass
class ProofGeneratorError(Exception):
    error: ProofGeneratorErrorType


class ProofGenerator:
    """
    A class for generating proofs.
    """

    input_objects: list[GeoObject]
    """The problem's objects."""
    input_predicates: list[Predicate]
    """Predicates on the problem's objects."""
    target_objects: list[GeoObject] | None
    """The objects that should be created."""
    target_predicates: list[Predicate] | None
    """The predicates the created objects should satisfy."""
    checker: ProofChecker
    """The object tracking all the objects and predicates created."""
    proof_steps: list[Step]
    """The generated proof."""
    sig_dag: SignatureDag
    """An object for finding new theorems."""
    step_queue: list[StepSuggestion]
    """The queue of next steps considered by the proof generator."""
    used_theorems: set[tuple[str, tuple[GeoObject, ...]]]
    """The set of theorems that were already used by the proof generator."""
    actions_per_step: int | Callable[[int], int]
    """The number of theorems and constructions to introduce every step."""
    verbose: bool
    """Whether to print debug information."""
    processed_objects: set[GeoObject]
    """All objects that have been processed by the proof generator."""
    all_names: set[str]
    """All names used either in the checker or by any step in the step queue."""

    def __init__(self, proof: Proof, actions_per_step: int | Callable[[int], int] = 3, verbose=False):
        self.input_objects = list(proof.assumption_objects.values())
        self.input_predicates = list(proof.starting_predicates())
        self.target_objects = list(proof.target_objects.values())
        self.target_predicates = proof.target_predicates
        self.checker = ProofChecker(proof)
        self.checker.geometry_tracker.load_assumptions(proof)
        self.verbose = verbose
        self.proof_steps = []
        # self.sig_matcher = SignatureMatcher(self.checker, verbose=self.verbose)
        self.sig_dag = SignatureDag(
            self.checker.geometry_tracker, list(Theorem.all_theorems().values()) + list(get_constructions().values())
        )
        self.used_theorems = set()
        self.actions_per_step = actions_per_step
        self.processed_objects = set()
        self.step_queue = []
        self.all_names = set()

    def run(self, step_count: Optional[int] = None, timeout: Optional[int] = None):
        """
        Attempts to find a proof.
        """
        start_time = time.process_time()
        try:
            i = 0
            while step_count is None or len(self.proof_steps) < step_count:
                i += 1
                if self.verbose:
                    print(f'Step {i}')
                if self.check_finished():
                    if self.verbose:
                        print('Success!')
                    return
                if timeout is not None and time.process_time() - start_time > timeout:
                    raise ProofGeneratorError(ProofGeneratorErrorType.Timeout)
                # self.add_default_objects()
                self.update_matcher()

                actions_per_step = (
                    self.actions_per_step
                    if isinstance(self.actions_per_step, int)
                    else self.actions_per_step(len(self.proof_steps))
                )
                if self.verbose:
                    print(f'=========== {i}th try of finding up to {actions_per_step} steps =========')
                steps = self.find_steps(actions_per_step)
                if self.verbose:
                    print(f'=========== found {len(steps)} steps =========')
                if len(steps) == 0:
                    raise ProofGeneratorError(ProofGeneratorErrorType.NoMoreSteps)
                self.proof_steps.append(CommentStep(f"Step {i} - Found {len(steps)} steps"))
                for step in steps:
                    match step:
                        case ObjDefineStep() as obj_step:
                            if self.verbose:
                                print(f'Adding construction step {obj_step}')
                            self.proof_steps.append(obj_step)
                            self.checker.add_step(obj_step)
                        case TheoremStep() as theo_step:
                            # Fixing the names of theorem objects.
                            self.proof_steps.append(theo_step)
                            self.checker.add_step(theo_step)
                        case _:
                            raise GeometryError(f'Unknown step type: {step}')
            raise ProofGeneratorError(ProofGeneratorErrorType.StepLimitReached)
        except KeyboardInterrupt:
            raise

    def find_steps(self, step_count: int = 1) -> list[ObjDefineStep | TheoremStep]:
        """
        Finds a step to take in the proof.
        """
        found_steps: list[TheoremStep | ObjDefineStep] = []
        found_predicates = set(self.checker.geometry_tracker.all_predicates())

        unique_objects = set(self.checker.geometry_tracker.unique_objects())
        all_objects = set(self.checker.geometry_tracker.all_objects())

        while self.step_queue:
            step = heapq.heappop(self.step_queue)

            # If the step is not ready yet we refine its score and push back to the step_queue
            if not step.is_ready():
                step.refine_score(self.checker)
                heapq.heappush(self.step_queue, step)
                continue

            # If one of the step inputs is not one of the unique objects of the checker then we skip this step.
            # (since we'll meet it agian with an equivalent objects which are all in the unique objects list of the checker)
            if any(inp not in unique_objects for inp in step.inputs.values()):
                continue

            # convert the step suggestion to actionable step
            fin_step = step.to_step(self.checker, self.all_names)

            # dealing with Definition step.
            if isinstance(fin_step, ObjDefineStep):
                obj = fin_step.left_hand
                if is_trivial(obj):
                    continue
                if obj in all_objects:
                    # The object is already known.
                    continue
                if isinstance(obj, ConstructionObject) and any(comp not in unique_objects for comp in obj.components):
                    # The object uses components that are equal to others.
                    continue
                found_steps.append(fin_step)
                # print(f'Found step {fin_step.to_language_format()} with score {step.score}.')

            # dealing with theorem step
            elif isinstance(fin_step, TheoremStep):
                # Making sure that there are new predicates remaining in the step.
                if all(
                    pred in found_predicates
                    or is_trivial(pred)
                    or self.checker.geometry_tracker.contains_predicate(pred)
                    for pred in fin_step.result_predicates
                ):
                    continue
                if self.should_skip_theorem_step(fin_step):
                    continue
                # print(f'Found step {fin_step.to_language_format()} with score {step.score}.')
                found_steps.append(fin_step)
                for pred in get_result_predicates(fin_step):
                    # if pred.name == 'exists':
                    #     print(f'draw {pred.components[0]} as result predicate of the step {fin_step}')
                    found_predicates.add(pred)
                # Printing the explanation for the step score.
                # print(f'Final score: {step.step_score(self.checker, verb=True)}')
            else:
                raise GeometryError(f'Unknown step type: {fin_step}!')

            if len(found_steps) == step_count:
                break

        return found_steps

    def add_default_objects(self):
        """
        Adds default objects to the proof checker, to allow fast processing.

        Currently adding:
        * All line angles.
        * All lines.
        * All distances.

        Which is the minimum to start doing angle arithmetic and triangle congruences.
        """
        unprocessed_objects = [
            obj for obj in self.checker.geometry_tracker.all_objects() if obj not in self.processed_objects
        ]
        unprocessed_unique = [
            obj for obj in self.checker.geometry_tracker.unique_objects() if obj not in self.processed_objects
        ]

        new_names = set()

        for obj in unprocessed_objects:
            self.processed_objects.add(obj)
            self.all_names.add(obj.name)
            new_names.add(obj.name)

        # When adding new objects, we update steps that were penalized for introducing them.
        if len(new_names) > 0:
            updated_steps = []
            for step in self.step_queue:
                if step.construction_penalties is None or len(step.construction_penalties.keys() & new_names) == 0:
                    continue
                new_score = step.score
                new_penalties = dict(step.construction_penalties)
                for name in new_names:
                    if name in new_penalties:
                        new_score -= new_penalties[name]
                        del new_penalties[name]

                updated_steps.append(StepSuggestion(step.step, step.inputs, new_score, step.phase, new_penalties))

            for step in updated_steps:
                heapq.heappush(self.step_queue, step)

        # points = [obj for obj in unprocessed_unique if obj.type == POINT]

        # for p in points:
        #     for old_p in points:
        #         dist = ConstructionObject.from_args('distance', (p, old_p))
        #         self.checker._geometry_tracker.get_object(dist, ADD_CFG)

    def check_finished(self) -> bool:
        """
        Returns whether the proof generator managed to prove the target theorem.
        """
        # If we have proved a contradiction, we are done.
        if self.checker.geometry_tracker.contains_predicate(predicate_from_args('false', ())):
            raise ProofGeneratorError(ProofGeneratorErrorType.Contradiction)

        if self.target_objects is not None and self.target_predicates is not None:
            # TODO: This doesn't yet find cases where the target objects are constructed under a different name.
            mapped_predicates = [
                self.checker.geometry_tracker.get_predicate(pred, TRUST_NO_ADD_CFG) for pred in self.target_predicates
            ]
            return all(self.checker.geometry_tracker.contains_predicate(pred) for pred in mapped_predicates)

        return False

    def update_matcher(self):
        """
        Updates the signature matcher, and gathers all new steps from the matches into the signature matcher.
        """
        self.sig_dag.update()
        for step, match_ in self.sig_dag.new_steps():
            if isinstance(step, Theorem):
                new_step = StepSuggestion(step, match_)
                heapq.heappush(self.step_queue, new_step)

    def should_skip_theorem_step(self, theorem_step: TheoremStep) -> bool:
        theorem = Theorem.all_theorems()[theorem_step.theorem_name]

        if len(theorem.required_embedding_predicates) > 0 and self.checker.geometry_tracker.embedding_tracker is None:
            return True
        for predicate in theorem.required_embedding_predicates:
            substituted_predicate = predicate.substitute(dict(zip(theorem.signature, theorem_step.inputs)))
            value = self.checker.geometry_tracker.embedding_tracker.evaluate_predicate(substituted_predicate)
            if value != EmbeddedPredicateValue.Correct:
                return True

        for condition in theorem.trivial_if_equal_conditions:
            obj_names = [obj.name for obj in theorem.signature]
            for lhs, rhs in zip(*condition):
                lhs_index = obj_names.index(lhs)
                rhs_index = obj_names.index(rhs)
                lhs_sub = self.checker.geometry_tracker.get_object(theorem_step.inputs[lhs_index], CHECK_CFG)
                rhs_sub = self.checker.geometry_tracker.get_object(theorem_step.inputs[rhs_index], CHECK_CFG)
                if lhs_sub != rhs_sub:
                    break
            else:
                ############### comment for now ##############################################
                # print(f'Found trivial theorem step! ({theorem_step})')
                return True

        return False


def validate_proof(proof: Proof):
    """
    Checks that the checker can find all theorem steps used by the given proof.
    """
    proof_gen = ProofGenerator(proof)
    checker = proof_gen.checker

    failed_steps = []
    failed_conclusion = False

    all_steps: list[tuple[Theorem | Construction, frozendict[GeoObject, GeoObject]]] = []

    for idx, step in enumerate(proof.steps):
        if isinstance(step, TheoremStep):
            theorem = Theorem.from_name(step.theorem_name)
            assert theorem is not None

            subs = {
                sig: checker.geometry_tracker.get_object(inp, CHECK_CFG)
                for sig, inp in zip(theorem.signature, step.inputs)
            }

            for pred in theorem.required_predicates:
                for obj in involved_objects(pred):
                    if isinstance(obj, EquationObject):
                        continue
                    obj = obj.substitute(subs)
                    if obj not in proof_gen.checker.geometry_tracker._processed_objects and obj.type != LITERAL:
                        proof_gen.checker.geometry_tracker.get_object(obj, CHECK_CFG)
                        print(f'Adding object {obj}')

            if all(checker.geometry_tracker.contains_predicate(pred) for pred in step.result_predicates):
                continue
            print(f'Attempting to match {step.to_language_format()}')
            proof_gen.sig_dag.update()
            all_steps.extend(proof_gen.sig_dag.new_steps())

            assert theorem is not None

            for found_step, inputs in all_steps:
                if not isinstance(found_step, Theorem):
                    continue
                if step.theorem_name != found_step.name:
                    continue
                if step.inputs == [inputs[sig] for sig in found_step.signature]:
                    break
            else:
                print('Failed.')
                failed_pattern = next(
                    pat
                    for pat, pat_step in proof_gen.sig_dag.step_patterns.items()
                    if pat_step.name == step.theorem_name
                )
                if isinstance(failed_pattern, IntersectPattern):
                    print('Sub patterns:')
                    for sub_pattern in failed_pattern.components:
                        for mtch in sub_pattern.all_matches.to_dict(KNOWN_KEYS):
                            if all(
                                sig not in mtch or mtch[sig] == inp for sig, inp in zip(theorem.signature, step.inputs)
                            ):
                                break
                        else:
                            print('Bad sub-pattern:')
                            print(sub_pattern.full_repr())

                failed_steps.append(step)

        proof_gen.checker.add_step(step)

    proof_gen.update_matcher()
    if not proof_gen.check_finished():
        failed_conclusion = True

    failed_repr = ''
    if failed_steps:
        failed_repr = "\n".join(failed.to_language_format() for failed in failed_steps)
        failed_repr = f'Failed to find steps:\n{failed_repr}\n'
    if failed_conclusion:
        failed_repr += 'Failed to prove conclusion.'

    if failed_steps or failed_conclusion:
        raise GeometryError(failed_repr)


def generate_random_proof(
    path: Path,
    out_path_pattern: str,
    out_dir: Path,
    job_idx: int,
    shuffle=False,
    timeout: int | None = None,
    proofs_per_problem=5,
    quiet_fail: bool = False,
):
    """
    Attempts to generate a proof.

    Parameters:
    * `path`: The path to the problem.
    * `out_path_pattern`: The pattern for output paths related to the problem.
    * `shuffle`: Whether to shuffle the problems and proofs.
    * `timeout`: The maximal amount of time to allocate for each proof.
    * `proofs_per_problem`: The number of proofs to attmept to create for each problem.
    """
    if len(path.suffixes) == 0:
        return
    if path.suffixes[0] == '.proof':
        return

    out_lock = Path(out_path_pattern.format('lock'))
    log_addr = out_dir / f'log_{job_idx}.txt'
    try:
        # Making sure the output directory exists.
        # This sometimes raises an exception when there are collisions.
        os.makedirs(str(Path(out_path_pattern).parent), exist_ok=True)
    except:
        ...

    try:
        if out_lock.exists():
            return
        try:
            match path.suffix:
                case '.txt':
                    base = Proof.parse(path.open().read(), False)
                case '.pkl':
                    base = Proof.parse(pickle.load(path.open('rb'))['text'], False)
                case _:
                    # Ignoring unknown files.
                    return

        except (KeyError, GeometryError) as e:
            print(f'Failed to parse {path.stem}: {e}')
            return

        if shuffle:
            random.shuffle(base.assumption_predicates)
            random.shuffle(base.auxiliary_predicates)

        # Converting empty proofs to unprovable proofs.
        if len(base.target_predicates) == 0:
            base.target_predicates.append(predicate_from_args('false', ()))

        t = time.process_time()
        with log_addr.open('a') as f:
            f.write(f'Process {multiprocessing.current_process().name} starting {path.name} at time {t:.1f}\n')
        out_lock.touch()

        proof_gen = ProofGenerator(base, actions_per_step=lambda steps: 3 * int(10 // (steps + 1) + 1))
        proof_gen.run(step_count=None, timeout=timeout)

        new_proof = base.shallow_copy()
        new_proof.steps = proof_gen.proof_steps  # type: ignore

        untrim_addr = out_path_pattern.format('untrimmed')
        with open(untrim_addr, 'w') as f:
            f.write(new_proof.to_language_format())

        # Checking that all the steps are legal.
        checker = ProofChecker(new_proof)
        new_proof.target_predicates = []
        checker.check()
        new_proof.target_predicates = base.target_predicates

        # Trimming the proof.

        trimmed_proofs = max_depth_trim(new_proof, target_count=proofs_per_problem)
        for idx, trimmed_proof in enumerate(trimmed_proofs):
            # Making sure that the trimmed proof is valid.
            checker = ProofChecker(trimmed_proof)
            checker.check()

            if shuffle:
                trimmed_proof = trimmed_proof.shuffled()
            # Making sure it remains valid when shuffled.
            checker = ProofChecker(trimmed_proof)
            checker.check()

            out_path = Path(out_path_pattern.format(idx))
            with out_path.open('w') as f:
                f.write(trimmed_proof.to_language_format())
        with log_addr.open('a') as f:
            t_fin = time.process_time()
            f.write(
                f'Process {multiprocessing.current_process().name} finished {path.name} at time {t_fin:.1f} ({t_fin - t:.1f})\n'
            )

    except KeyboardInterrupt as e:
        if out_lock.exists():
            out_lock.unlink()
        time.sleep(0.1)

    except (ProofGeneratorError, ProofCheckError, AssertionError, IllegalObjectError, GeometryError) as e:
        if out_lock.exists():
            out_lock.unlink()
        print(f'Encountered {e}')

        if not quiet_fail:
            identifier = str(path).split('_')[-1].split('.')[0]

            with open(f'proof_fail_{identifier}.jl', 'w') as f:
                base.steps = proof_gen.proof_steps  # type: ignore
                f.write(base.to_language_format())
                f.write('\n')
                for ln in repr(e).split('\n'):
                    f.write(f'# {ln}\n')
            with log_addr.open('a') as f:
                t_fin = time.process_time()
                f.write(
                    f'Process {multiprocessing.current_process().name} failed {path.name} at time {t_fin:.1f} ({t_fin - t:.1f}) with exception {e}\n'
                )
            raise


def prove_all_assumptions(
    assumption_path: Path,
    out_dir: Path,
    multiprocess: bool,
    shuffle=False,
    job_idx: int | None = None,
    job_count: int | None = None,
    timeout: int | None = None,
    proofs_per_problem: int = 1,
    quiet_fail: bool = False,
):
    """
    Proves all assumptions in the given directory.

    Parameters:
    * `dir`: The directory containing the problem files.
    * `multiprocess`: Whether to use multiprocessing to prove multiple problems in parallel.
    * `shuffle`: Whether to shuffle the names and assumption order in the problem input.
    * `job_idx`: If several jobs were used to search for proofs, then this stores the index of the job.
    * `job_count`: If several jobs were used to search for proofs, then this is the total count of jobs used.
    """
    print(f'Assumption path exists: {assumption_path.exists()}')
    print(f'Searching for geometry problems in {assumption_path}/**/*.txt')
    assumption_paths = glob.glob(f'{assumption_path}/**/*.txt', recursive=True) + glob.glob(
        f'{assumption_path}/**/*.pkl', recursive=True
    )
    print(f'Assumption paths: {len(assumption_paths)}')

    if job_count is not None and job_idx is not None:
        assumption_paths = [
            path
            for path in assumption_paths
            if (int(hashlib.blake2b(str(path).encode('utf-8')).hexdigest()[:8], 16) % job_count) == job_idx
        ]

    print(f'For given job: {len(assumption_paths)}')
    assumption_paths = [Path(path) for path in (assumption_paths) if 'proof.txt' not in str(path)]

    out_paths = [
        str(out_dir / '/'.join(path.parts[len(assumption_path.parts) : -1]) / f'{path.stem}_{{}}.proof.txt')
        for path in (assumption_paths)
    ]
    args = [
        (in_path, out_path, out_dir, job_idx or 0, shuffle, timeout, proofs_per_problem, quiet_fail)
        for in_path, out_path in (zip(assumption_paths, out_paths))
    ]
    print('Starting!')
    if multiprocess:
        print(f'Using {os.cpu_count()} processes.')
        with multiprocessing.Pool() as pool:
            pool.starmap(generate_random_proof, args)
    else:
        for arg in args:
            generate_random_proof(*arg)


def prove(base: Proof, interactive: bool, verbose: bool) -> Proof:
    if base.embedding is not None:
        collector = NonDegeneracyPrediateCollector()
        non_degenerecy_predicates = collector.collect(base.assumption_objects, base.embedding)
        base.auxiliary_predicates.extend(non_degenerecy_predicates)

    proof_gen = ProofGenerator(base, actions_per_step=10000, verbose=verbose)

    try:
        proof_gen.run()
        completed_proof = base.shallow_copy()
        completed_proof.steps = proof_gen.proof_steps
        return completed_proof
    except (KeyboardInterrupt, ProofGeneratorError, ProofCheckError) as e:
        base.steps = proof_gen.proof_steps
        with (BASE_PATH / 'rules/proof_samples/proof_fail.jl').open('w') as f:
            f.write(base.to_language_format())
            f.write('\n')
            for ln in repr(e).split('\n'):
                f.write(f'# {ln}\n')

        if interactive and (
            isinstance(e, KeyboardInterrupt)
            or (isinstance(e, ProofGeneratorError) and e.error == ProofGeneratorErrorType.NoMoreSteps)
        ):
            print(f'Stopped due to {e}.')
            print('Beginning interactive session...')
            InteractivePredicateChecker(proof_gen.checker.geometry_tracker).run()
        raise e
