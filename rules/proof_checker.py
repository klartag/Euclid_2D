import time
from pathlib import Path
import time

from tqdm import trange

from rules.proof.geometry_problem import GeometryProblem

from .embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPrediateCollector
from .embeddings.embedded_predicate_value import EmbeddedPredicateValue

from .interactive_predicate_checker import InteractivePredicateChecker

from .predicates.predicate_factory import predicate_from_args

from .geometry_trackers.geometry_tracker import GeometryTracker

from .proof_checker_utils import ADD_CFG, ADD_NO_TRUST_CFG, CHECK_CFG, TRUST_NO_ADD_CFG, unpack_predicate_full
from .geometry_trackers.geometry_tracker import involved_objects

from .theorem import Theorem
from .proof.document.geometry_document import GeometryDocument
from .proof.document.reader.document_reader import DocumentReader
from .proof.proof import Proof
from .proof.steps import AlmostAlwaysStep, AssertStep, CommentStep, ObjDefineStep, Step, TheoremStep

from . import rule_utils
from .rule_utils import ProofCheckError, R_EQN_TYPES
from .geometry_objects.geo_object import GeoObject
from .geometry_objects.equation_object import EquationObject
from .geometry_objects.construction_object import ConstructionObject
from .predicates.predicate import Predicate


def all_possibilities(pred: Predicate) -> set[Predicate]:
    """
    Finds a minimal set of predicates containing the given predicate, such that one of the predicates in the set is always true.
    Used in If-Steps to determine all conditions that should be checked.
    """
    match pred.name:
        case 'in' | 'not_in':
            return {predicate_from_args('in', pred.components), predicate_from_args('not_in', pred.components)}
        case 'equals' | 'not_equals':
            return {predicate_from_args('not_equals', pred.components), predicate_from_args('equals', pred.components)}
        case 'equals_mod_360' | 'not_equals_mod_360':
            return {
                predicate_from_args('equals_mod_360', pred.components),
                predicate_from_args('not_equals_mod_360', pred.components),
            }
        case 'between':
            a, b, c = pred.components
            return {
                predicate_from_args('between', (a, b, c)),
                predicate_from_args('between', (b, a, c)),
                predicate_from_args('between', (a, c, b)),
                predicate_from_args('not_in', (a, ConstructionObject.from_args('Line', (b, c)))),
            }
        case _:  # TODO: This seems to be a bug. The correct thing would be to return None here.
            return set()


class ProofChecker:
    """
    A class that checks that a proof is valid.
    """

    problem: GeometryProblem
    checked_steps: int
    geometry_tracker: GeometryTracker
    """Tracks when automatic theorems can be applied. The automatic predicates are added after a step is applied."""

    def __init__(self, problem: GeometryProblem):
        self.problem = problem
        self.checked_steps = 0

        self.geometry_tracker = GeometryTracker()

    def process_angle(self, angle: GeoObject):
        """
        Adds automatic theorems to an angle.

        The theorems added are:
        * `angle(A, B, C) == -angle(C, B, A)`

        Parameters:

        * `angle`: An angle to add theorems to.
        """
        if not isinstance(angle, ConstructionObject):
            return

        if angle.constructor.name != 'angle':
            return

        assert angle in self.geometry_tracker._processed_objects and angle in self.geometry_tracker._objects

        a, b, c = angle.components
        if a != c:
            rev_angle = self.geometry_tracker.get_object(ConstructionObject.from_args('angle', (c, b, a)), ADD_CFG)
            assert rev_angle in self.geometry_tracker._processed_objects and rev_angle in self.geometry_tracker._objects
            self.geometry_tracker._linear_algebra._real_equations.add_relation({angle: 1, rev_angle: 1})
            self.geometry_tracker._linear_algebra._mod_360_equations.add_relation({angle: 1, rev_angle: 1})

    def process_orientation(self, ori: GeoObject):
        """
        Adds automatic theorems to an orientation.
        The theorems currently added are:
        * `orientation(A, B, C) + orientation(C, B, A) == 0 mod 360`
        * `2 * orientation(A, B, C) == 180 mod 360`

        Parameters:
        * `ori`: An orientation to add theorems to.
        """
        if not isinstance(ori, ConstructionObject) or ori.constructor.name != 'orientation':
            return

        a, b, c = ori.components
        self.geometry_tracker.add_predicate(
            predicate_from_args('not_collinear', (a, b, c)), ADD_CFG, 'Since they have an orientation.'
        )

        rev = self.geometry_tracker.get_object(
            ConstructionObject.from_args('orientation', ori.components[::-1]), ADD_CFG
        )
        assert rev in self.geometry_tracker._processed_objects and rev in self.geometry_tracker._objects

    def process_object(self, obj: GeoObject):
        """
        Adds all conclusions derived from a legal object.
        This function is called only when the object is deemed legal and should be added.
        """
        if obj in self.geometry_tracker._processed_objects:
            return
        if obj.name == '0':
            return
        print(f'Processing object {obj}')
        self.geometry_tracker._processed_objects.add(obj)

        for equiv in list(self.geometry_tracker._objects.get_equivalences(obj)):
            self.process_object(equiv)

        if isinstance(obj, ConstructionObject):
            # We add the requirements, since objects in the assumptions might not have all requirements.
            for req in obj.requirements():
                self.geometry_tracker.add_predicate(req, ADD_CFG, f'Requirement of {obj}')
            for comp in obj.components:
                self.process_object(
                    self.geometry_tracker.get_object(comp, ADD_CFG),
                )
            for pred in obj.conclusions():
                self.geometry_tracker.add_predicate(pred, ADD_CFG, f'conclusion of {obj}')

            for req_preds, res_preds in obj.possible_conclusions():
                if all(self.geometry_tracker.contains_predicate(pred) for pred in req_preds):
                    for pred in res_preds:
                        self.geometry_tracker.add_predicate(pred, ADD_CFG, f'Possible conclusion of {obj}')

            for pred in self.geometry_tracker.numeric_tracker.add_construction(obj):
                self.geometry_tracker.add_predicate(pred, ADD_CFG, 'From numeric tracker')

        if isinstance(obj, EquationObject):
            for comp in involved_objects(obj):
                self.process_object(
                    self.geometry_tracker.get_object(comp, ADD_CFG),
                )

        match obj.type:
            case rule_utils.ANGLE:
                self.process_angle(obj)
            case rule_utils.ORIENTATION:
                self.process_orientation(obj)

    def _add_obj_define_step(self, step: ObjDefineStep):
        """
        Checks that the object definition step is legal, and adds the equality between the two sides.
        The legality should be verified by the parser, since things are ill-defined otherwise.
        @param step: The object definition data.
        """
        if step.right_hand is not None:
            if step.left_hand.type != step.right_hand.type:
                raise ProofCheckError(
                    f'In object definition step {step}, left type={step.left_hand.type} right type={step.right_hand.type}.'
                )

            # In an object definition step, we have no guarantee that the right-hand side is legal.
            reason = f'object definition in the step: {step}'
            self.geometry_tracker.add_predicate(
                predicate_from_args('equals', (step.left_hand, step.right_hand)),
                ADD_NO_TRUST_CFG,
                reason,
            )
        else:
            self.geometry_tracker.get_object(step.left_hand, ADD_NO_TRUST_CFG)

        defined_objects = (
            involved_objects(step.left_hand) | involved_objects(step.right_hand)
            if step.right_hand != None
            else involved_objects(step.left_hand)
        )
        predicate = predicate_from_args('exists', tuple(defined_objects))
        self.geometry_tracker.add_predicate(
            predicate, ADD_CFG, 'Objects we introduce or define should be marked as existing'
        )
        print(f'draw {defined_objects} since we define them in {step}')

    def _add_theorem_step(self, step: TheoremStep, skim: bool) -> str | None:
        """
        Checks that the theorem can be applied, and that the predicates given actually follow from the theorem.
        @param step: The theorem step data.

        Return:

        Whether the step was added sucessfully.
        """
        theorem = Theorem.from_name(step.theorem_name)
        if theorem is None:
            return f'Theorem {step.theorem_name} does not exist.'

        inputs = [self.geometry_tracker.get_object(step_inp, ADD_NO_TRUST_CFG) for step_inp in step.inputs]

        # Making sure that the theorem was applied on the correct number of inputs.
        if len(inputs) != len(theorem.signature):
            return f'In step {step}, argument count to theorem is incorrect.'

        # Making sure that the input types are correct.
        substitutions: dict[GeoObject, GeoObject] = {}
        for theorem_in, step_in in zip(theorem.signature, inputs):
            if (theorem_in.type != step_in.type) and not (step_in.type == 'Literal' and theorem_in.type in R_EQN_TYPES):
                return f'In step {step}, types are incorrect: {theorem.signature} != {[inp.type for inp in inputs]}.'
            substitutions[theorem_in] = step_in

        if not skim:
            # Making sure that all predicates are satisfied.
            for pred in theorem.required_predicates:
                substituded_pred = pred.substitute(substitutions)
                if not self.geometry_tracker.contains_predicate(substituded_pred, config=ADD_NO_TRUST_CFG):
                    return f'In step {step}, required predicate {substituded_pred} is not satisfied.\n{pred.name} {pred.name == "equals"}'
                if self.geometry_tracker.embedding_tracker is not None:
                    pred_value = self.geometry_tracker.embedding_tracker.evaluate_predicate(substituded_pred)
                    if pred_value == EmbeddedPredicateValue.Incorrect:
                        return f'In step {step}, required predicate {substituded_pred} is not satisfied in the embedding.\n{pred.name} {pred.name == "equals"}'
                    elif pred_value == EmbeddedPredicateValue.Undefined:
                        return f'In step {step}, required predicate {substituded_pred} is undefined in the embedding.\n{pred.name} {pred.name == "equals"}'
            for pred in theorem.required_embedding_predicates:
                if self.geometry_tracker.embedding_tracker is None:
                    return f'In step {step}, there are required embedding predicates, but there is no embedding!'
                substituded_pred = pred.substitute(substitutions)
                pred_value = self.geometry_tracker.embedding_tracker.evaluate_predicate(substituded_pred)
                if pred_value != EmbeddedPredicateValue.Correct:
                    return f'In step {step}, required embedding predicate {substituded_pred} is not satisfied in the embedding.\n{pred.name} {pred.name == "equals"}'

        # All predicates are satisfied, and all objects are legal.
        # The results are known to exist.

        outputs = [self.geometry_tracker.get_object(step_out, CHECK_CFG) for step_out in step.result_objects]

        for result_predicate in theorem.result_predicates:
            pred = result_predicate.substitute(substitutions)
            if self.geometry_tracker.embedding_tracker is not None:
                pred_value = self.geometry_tracker.embedding_tracker.evaluate_predicate(pred)
                if pred_value == EmbeddedPredicateValue.Incorrect:
                    return f'In step {step}, result predicate {pred} is not satisfied in the embedding.\n{pred.name} {pred.name == "equals"}'
            for obj in pred.involved_objects():
                predicate = predicate_from_args('exists', (obj,))
                self.geometry_tracker.add_predicate(predicate, ADD_CFG, 'Marking a processed object as existing')

        for result_object in theorem.result_objects:
            obj = result_object.substitute(substitutions)
            predicate = predicate_from_args('exists', (obj,))
            self.geometry_tracker.add_predicate(predicate, ADD_CFG, 'Marking a processed object as existing')

        # Making sure that the output types are correct.
        if not skim:
            if len(step.result_objects) != len(theorem.result_objects):
                return f'In step {step}, not enough objects were constructed.'
            for theorem_out, step_out in zip(theorem.result_objects, outputs):
                if theorem_out.type != step_out.type:
                    return f'In step {step}, constructed object had incorrect type.'
                substitutions[theorem_out] = step_out

        # Making sure that the predicates specified by the step follow from the theorem, and adding them.
        # The step is allowed (And probably encouraged) not to use all predicates proved by the theorem.
        # We substitute twice because getting the predicates the first time could have added equalities,
        # and the identity of the predicates changed after that.

        real_result_predicates = {
            self.geometry_tracker.get_predicate(pred.substitute(substitutions), TRUST_NO_ADD_CFG)
            for pred in theorem.result_predicates
        }
        needed_result_predicates = [
            self.geometry_tracker.get_predicate(step_pred, TRUST_NO_ADD_CFG) for step_pred in step.result_predicates
        ]

        # Adding the results of all theorems.
        for step_pred in needed_result_predicates:
            deep_search = [unpack_predicate_full(pred) for pred in real_result_predicates]
            deep_search = set.union(*deep_search)
            deep_search_and_real_result_predicates = set.union(real_result_predicates, deep_search)
            if step_pred not in deep_search_and_real_result_predicates:
                return (
                    f'\nIn step {step}:\n'
                    f'Predicate {step_pred} does not follow from theorem. \n'
                    f'Theorem results: {[self.geometry_tracker.get_predicate(res_pred.substitute(substitutions), TRUST_NO_ADD_CFG) for res_pred in theorem.result_predicates]}\n'
                    f'Substitutions: { {obj: self.geometry_tracker.get_object(obj, TRUST_NO_ADD_CFG) for obj in step_pred.components} }'
                )
            reason = f'consequence of the theorem step: {step.theorem_name}'
            self.geometry_tracker.add_predicate(step_pred, ADD_CFG, reason)  # .deeper(False)

        return None

    def _add_assert_step(self, step: AssertStep):
        """
        Adds a step that assrets that some predicate has been proved.
        @step: The assertion step.
        """
        for pred in step.predicates:
            if not self.geometry_tracker.contains_predicate(pred, config=ADD_NO_TRUST_CFG):
                raise ProofCheckError(f'Step {step} requires predicate {pred} which was not proved.')
            # We add the predicate explicitly.
            # Although the predicate might have been proved implicitly, such as by a linear algebra tracker,
            # here we state it has been proved for If steps (Which could also stand to have a "Thus" section to do this).
            self.geometry_tracker._asserted_predicates.add(pred)
            self.geometry_tracker.add_unpacked_predicate(pred, ADD_CFG, reason='assertion predicate')  # .deeper(False)

    def _add_almost_always_step(self, step: AlmostAlwaysStep):
        """
        Adds an `AlmostAlwaysStep`.
        """
        for pred in step.predicates:
            if not pred.is_open():
                raise ProofCheckError(f'Step {step} claimed that a closed condition {pred} is almost always true.')
            # Attempting to add the objects. They are not trusted.
            for obj in pred.components:
                self.geometry_tracker.get_object(obj, ADD_NO_TRUST_CFG)

            self.geometry_tracker.add_predicate(pred, ADD_CFG, 'Asserted in almost always step.')  # .deeper(False)

    def shallow_copy(self) -> 'ProofChecker':
        """
        Returns a shallow copy of the proof checker.
        """
        res = ProofChecker(self.problem.shallow_copy())
        res.geometry_tracker = self.geometry_tracker.clone()
        res.checked_steps = self.checked_steps
        return res

    def add_step(self, step: Step, skim=False):
        """
        Handles a single theorem step.
        """
        try:
            match step:
                case ObjDefineStep():
                    self._add_obj_define_step(step)

                case TheoremStep():
                    if (err := self._add_theorem_step(step, skim)) is not None:
                        raise ProofCheckError(err)

                case AssertStep():
                    if not skim:
                        self._add_assert_step(step)

                case AlmostAlwaysStep():
                    self._add_almost_always_step(step)

                case CommentStep():
                    pass

                case _:
                    raise NotImplementedError(f'Proof checker received illegal step: {step}!')
        except Exception as e:
            error_message = f'Failed to add the step {step.to_language_format()}: '
            if e.args:
                e.args = (error_message + e.args[0], e.args[1:])
            else:
                e.args = (error_message,)
            raise e

    def load_proof(self):
        """
        Loads the proof's assumptions.
        """
        self.geometry_tracker.load_assumptions(self.problem)

    def check_proof_finished(self):
        # If we have found a contradiction, then the proof is valid.
        for pred in self.geometry_tracker._predicates:
            if pred.name == 'false':
                return

        # Making sure that the results follow.
        for pred in self.problem.statement.target_predicates:
            if not self.geometry_tracker.contains_predicate(pred):
                self.geometry_tracker.contains_predicate(pred)
                raise ProofCheckError(f'Required predicate {pred} was not proved.')

    def check_until_step(self, step, skim=False, verbose=False):
        step_count = step - self.checked_steps

        if step_count < 0:
            raise ProofCheckError(f'The first `{step}` steps have already been checked.')

        self.check_steps(step_count, skim=skim, verbose=verbose)

    def check_steps(self, step_count=None, skim=False, verbose=False):
        '''
        Checks the next `step_count` steps in the proof that have not yet been checked.
        If `step_count == None`, checks all of the remaining steps in the proof.
        '''
        steps_left = len(self.problem.proof.steps) - self.checked_steps

        if step_count == None:
            step_count = steps_left

        if step_count > steps_left:
            raise ProofCheckError(f"Cannot run {step_count} steps, as there are only {steps_left} steps left.")

        range_wrapper = trange if verbose else range

        for i in range_wrapper(self.checked_steps, self.checked_steps + step_count):
            try:
                step = self.problem.proof.steps[i]
                self.add_step(step, skim=skim)
                self.checked_steps += 1
            except ProofCheckError as e:
                e.args = (f'In line {i}, step={step}:\n{e.args[0]}',)
                raise

    def check(self, verbose=False):
        """
        Checks if the proof is correct, and throws a `ProofCheckError` if it is not.
        """
        self.load_proof()
        self.check_steps(verbose=verbose)
        self.check_proof_finished()


def check_proof(path: Path, verbose=False, interactive: bool = False):
    document = GeometryDocument(path)
    problem = DocumentReader().read(document, read_proof_body=True)
    if problem.embedding is not None:
        collector = NonDegeneracyPrediateCollector()
        non_degenerecy_predicates = collector.collect(problem.statement.assumption_objects, problem.embedding)
        problem.statement.auxiliary_predicates.extend(non_degenerecy_predicates)
    checker = ProofChecker(problem)
    try:
        checker.check(verbose)
    except ProofCheckError as e:
        if interactive:
            print(f'Stopped due to {e}.')
            print('Beginning interactive session...')
            InteractivePredicateChecker(checker.geometry_tracker).run()
        raise e
    print('Proof checked successfully!')


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Verifies that proofs are correct.')
    parser.add_argument('path', help='The path of the problem file to verify.', type=Path)
    parser.add_argument('-v', help='Prints debug information', action='store_true')
    parser.add_argument(
        '--interactive',
        help='When a proof fails due to NoMoreSteps or a KeyboardInterrupt, allows the user to check what was proved.',
        action='store_true',
    )

    args = parser.parse_args()

    start_time = time.perf_counter()
    check_proof(args.path, verbose=args.v, interactive=args.interactive)
    print(f'Checked in {round(time.perf_counter() - start_time, 2)} seconds')


def interactive_main():
    import argparse

    parser = argparse.ArgumentParser(description='Loads a proof into the Interactive Predicate Checker.')
    parser.add_argument('path', help='The path of the problem file to load.', type=Path)
    parser.add_argument('-v', help='Prints debug information', action='store_true')

    args = parser.parse_args()

    document = GeometryDocument(args.path)
    problem = DocumentReader().read(document, read_proof_body=True)

    if problem.embedding is not None:
        collector = NonDegeneracyPrediateCollector()
        non_degenerecy_predicates = collector.collect(problem.statement.assumption_objects, problem.embedding)
        problem.statement.auxiliary_predicates.extend(non_degenerecy_predicates)

    checker = ProofChecker(problem)
    try:
        checker.check(False)
        print(f'Successfully loaded proof steps.')
    except ProofCheckError as e:
        print(f'Stopped due to {e}.')
    print('Beginning interactive session...')
    InteractivePredicateChecker(checker.geometry_tracker).run()
