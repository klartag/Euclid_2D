from dataclasses import dataclass
from enum import Enum
import heapq
import time
from typing import Callable, Optional
from frozendict import frozendict

from rules.proof.geometry_problem import GeometryProblem
from util import BASE_PATH

from ..embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPrediateCollector
from ..interactive_predicate_checker import InteractivePredicateChecker
from ..predicates.predicate import Predicate
from ..predicates.global_predicates import get_constructions
from ..predicates.predicate_factory import predicate_from_args
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.construction_object import Construction, ConstructionObject
from ..embeddings.embedded_predicate_value import EmbeddedPredicateValue
from ..proof.proof import Proof
from ..proof.steps import CommentStep, ObjDefineStep, Step, TheoremStep
from ..proof_checker import CHECK_CFG, TRUST_NO_ADD_CFG, ProofChecker, involved_objects
from ..proof_checker_utils import KNOWN_KEYS
from ..signature_dag import IntersectPattern, SignatureDag
from ..rule_utils import LITERAL, GeometryError, ProofCheckError
from ..theorem import Theorem

from .gen_utils import is_trivial
from .scores import StepSuggestion, get_result_predicates


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
    target_predicates: list[Predicate] | None
    """The predicates the problem should satisfy."""
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

    def __init__(self, problem: GeometryProblem, actions_per_step: int | Callable[[int], int] = 3, verbose=False):
        self.input_objects = list(problem.statement.objects.values())
        self.input_predicates = list(problem.statement.starting_predicates())
        self.target_predicates = list(problem.statement.target_predicates)
        self.checker = ProofChecker(problem)
        self.checker.geometry_tracker.load_assumptions(problem)
        self.verbose = verbose
        self.proof_steps = []
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

        if self.target_predicates is not None:
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


def validate_proof(problem: GeometryProblem):
    """
    Checks that the checker can find all theorem steps used by the given proof.
    """
    proof_gen = ProofGenerator(problem)
    checker = proof_gen.checker

    failed_steps = []
    failed_conclusion = False

    all_steps: list[tuple[Theorem | Construction, frozendict[GeoObject, GeoObject]]] = []

    for step in problem.proof.steps:
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


def prove(problem: GeometryProblem, interactive: bool, verbose: bool) -> GeometryProblem:
    if problem.embedding is not None:
        collector = NonDegeneracyPrediateCollector()
        non_degenerecy_predicates = collector.collect(problem.assumption_objects, problem.embedding)
        problem.statement.auxiliary_predicates.extend(non_degenerecy_predicates)

    proof_generator = ProofGenerator(problem, actions_per_step=10000, verbose=verbose)

    try:
        proof_generator.run()
        completed_problem = problem.shallow_copy()
        completed_problem.steps = proof_generator.proof_steps
        return completed_problem
    except (KeyboardInterrupt, ProofGeneratorError, ProofCheckError) as e:
        problem.steps = proof_generator.proof_steps
        with (BASE_PATH / 'rules/proof_samples/proof_fail.jl').open('w') as f:
            f.write(problem.to_language_format())
            f.write('\n')
            for ln in repr(e).split('\n'):
                f.write(f'# {ln}\n')

        if interactive and (
            isinstance(e, KeyboardInterrupt)
            or (isinstance(e, ProofGeneratorError) and e.error == ProofGeneratorErrorType.NoMoreSteps)
        ):
            print(f'Stopped due to {e}.')
            print('Beginning interactive session...')
            InteractivePredicateChecker(proof_generator.checker.geometry_tracker).run()
        raise e
