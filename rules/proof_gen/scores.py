import functools
import math
import random
import string

from frozendict import frozendict

from ..predicates.predicate import Predicate
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.construction_object import Construction, ConstructionObject
from ..proof import ObjDefineStep, TheoremStep
from ..proof_checker import ProofChecker, unpack_predicate_full
from ..rule_utils import GeometryError, union
from ..theorem import Theorem

# A small score is good.
CONSTRUCTION_PENALTY = 15  # Constructions are bad.
NESTED_CONSTRUCTION_SCORE = 5  # We don't like recursive constructions: midpoint(A, B) is fine, but midpoint(midpoint(A, B), C) is getting ridiculous.


def gen_name(all_names: set[str]) -> str:
    """
    Generates a new name not found in the given name set.
    """
    length = int(math.ceil(math.log(len(all_names), 26))) + 1 if len(all_names) > 0 else 1
    while (new_name := ''.join(random.choice(string.ascii_uppercase) for _ in range(length))) in all_names:
        pass
    all_names.add(new_name)
    return new_name


@functools.cache
def predicate_score(pred: Predicate) -> float:
    """
    Gives a score to the predicates.
    """
    depth = max(nested_construction_depth(comp) for comp in pred.components) if len(pred.components) > 0 else 0
    match pred.name:
        case 'between':
            # Betweens contain a lot of information.
            base_score = 5
        case 'collinear':
            base_score = 4
        case 'in':
            base_score = 3
        case 'equals' | 'equals_mod_360':
            if isinstance(pred.components[0], EquationObject) or isinstance(pred.components[1], EquationObject):  # type: ignore
                base_score = 1.5
            base_score = 3
        case 'false':
            base_score = 15
        case 'tangent':
            base_score = 6
        case _ if pred.is_open():
            # Open predicates are not interesting.
            base_score = 0
        case _:
            base_score = 1.5

    return base_score / (depth + 1)


@functools.cache
def nested_construction_depth(obj: GeoObject) -> int:
    """
    Returns the number of construction(construction(...)) chain used when definining the object.
    """
    match obj:
        case ConstructionObject():
            return 1 + max(nested_construction_depth(comp) for comp in obj.components)
        case EquationObject():
            return max(nested_construction_depth(obj.left), nested_construction_depth(obj.right))
    return 0


def get_constructions(
    step: TheoremStep | Theorem | Predicate | GeoObject | Construction, checked: set | None = None
) -> set[ConstructionObject]:
    """
    Gets the constructions directly involved in the step.
    """
    if checked is None:
        checked = set()

    if step in checked:
        return set()

    checked.add(step)

    match step:
        case Construction():
            return get_constructions(step(*step.signature), checked)
        case ConstructionObject():
            return (
                {step}
                | union(get_constructions(comp, checked) for comp in step.components)
                | union(get_constructions(comp, checked) for comp in step.conclusions())
            )
        case EquationObject():
            return get_constructions(step.left, checked) | get_constructions(step.right, checked)
        case GeoObject():
            return set()
        case Predicate():
            full_unpack = unpack_predicate_full(step)
            return union(union(get_constructions(comp, checked) for comp in pred.components) for pred in full_unpack)
        case Theorem():
            assert len(checked) == 1
            all_result_predicates = union(get_constructions(pred) for pred in step.result_predicates)
            all_required_predicates = union(get_constructions(pred) for pred in step.required_predicates)
            all_required_objects = union(get_constructions(obj) for obj in step.signature)

            return (all_result_predicates) - (all_required_objects | all_required_predicates)

        case TheoremStep():
            inputs = union(get_constructions(inp) for inp in step.inputs)
            res = union(get_constructions(res) for res in step.result_objects) | union(
                get_constructions(res) for res in step.result_predicates
            )
            return res - inputs


@functools.cache
def get_all_predicates(obj: Predicate | GeoObject) -> set[Predicate]:
    """
    Gets all predicates implied by the given object or predicate.

    Parameters:
    * `obj`: The object whose predicates are queried.
    """
    match obj:
        case ConstructionObject():
            return set(obj.conclusions()) | union(get_all_predicates(comp) for comp in obj.components)
        case EquationObject():
            return get_all_predicates(obj.left) | get_all_predicates(obj.right)
        case GeoObject():
            return set()
        case Predicate():
            full_unpack = unpack_predicate_full(obj)
            return full_unpack | union(
                union(get_all_predicates(comp) for comp in pred.components) for pred in full_unpack
            )


def get_required_predicates(
    step: TheoremStep | Theorem | ConstructionObject | Construction | GeoObject | Predicate,
) -> set[Predicate]:
    """
    Gets the predicates required by the given step.
    """
    match step:
        case Construction():
            return get_required_predicates(step(*step.signature))
        case ConstructionObject():
            return set(step.requirements()) | union(get_required_predicates(comp) for comp in step.components)
        case GeoObject():
            return set()
        case Predicate():
            return {step} | union(get_required_predicates(comp) for comp in step.components)
        case Theorem():
            all_required_predicates = union(get_required_predicates(pred) for pred in step.required_predicates)
            all_required_objects = union(get_required_predicates(obj) for obj in step.signature)

            return all_required_predicates | all_required_objects
        case TheoremStep():
            theo = Theorem.all_theorems()[step.theorem_name]

            subs = {obj: tar for obj, tar in zip(theo.signature, step.inputs)}
            all_required_predicates = union(
                get_required_predicates(pred.substitute(subs)) for pred in theo.required_predicates
            )
            all_required_objects = union(get_required_predicates(obj) for obj in step.inputs)

            return all_required_objects | all_required_predicates


def get_result_predicates(step: TheoremStep | Theorem | ConstructionObject | Construction) -> set[Predicate]:
    """
    Gets the predicates implied by the given step, that are also not required for it to be satisfied.
    """
    match step:
        case Construction():
            # Explicitly removing the required predicates is not strictly necessary,
            # but since weird things might happen with the inputs, we are extra careful.
            return set(step.result_predicates) - set(step.required_predicates)
        case ConstructionObject():
            # Ditto.
            return set(step.conclusions()) - set(step.requirements())
        case Theorem():
            return get_result_predicates(
                TheoremStep(step.name, step.signature, step.result_objects, step.result_predicates)
            )
        case TheoremStep():
            theo = Theorem.all_theorems()[step.theorem_name]

            subs = {obj: tar for obj, tar in zip(theo.signature, step.inputs)}
            all_required_predicates = union(
                get_required_predicates(pred.substitute(subs)) for pred in theo.required_predicates
            )
            all_required_objects = union(get_required_predicates(obj) for obj in step.inputs)

            all_result_predicates = union(get_all_predicates(obj) for obj in step.result_objects) | union(
                get_all_predicates(pred) for pred in step.result_predicates
            )

            return all_result_predicates - (all_required_objects | all_required_predicates)


@functools.cache
def cached_constructions(step: Theorem | Construction) -> set[ConstructionObject]:
    """
    A cached version of `get_constructions`.
    """
    return get_constructions(step)


@functools.cache
def theorem_score(theo: Theorem) -> float:
    return -max(predicate_score(pred) for pred in theo.result_predicates)


ALLOWED_CONSTRUCTORS = ('Line', 'angle', 'distance', 'orientation')


def construction_penalty(con: GeoObject | Construction, checker: ProofChecker) -> float:
    """
    Computes the score penalty of introducing the construction.
    """
    if isinstance(con, Construction):
        match con.name:
            case 'Line' | 'angle' | 'distance' | 'orientation':
                return 0
            case 'center' | 'intersection_of_tangent_line_and_circle':
                # These seem to be good points.
                return 3
            case _:
                return CONSTRUCTION_PENALTY
            # case 'intersection_of_tangent_line_and_circle':
            #     return 0
            # case _:
            #     return CONSTRUCTION_PENALTY
    elif isinstance(con, ConstructionObject):
        return construction_penalty(con.constructor, checker)
    else:
        return CONSTRUCTION_PENALTY


class StepSuggestion:
    """
    A class storing the steps and managing their scores.
    The score of the StepSuggestion has to be refined for several steps before it can be used.
    """

    """
    To compute fewer scores, I initially use for every StepSuggestion the expectation of the score of the theorem.
    Only if the expetation minus two standard deviations is sufficiently low, I compute the actual score and store 
    it in the score statistics.
    """
    step: Theorem | Construction
    inputs: frozendict[GeoObject, GeoObject]
    score: float
    phase: int
    construction_penalties: dict[str, float] | None

    def __init__(
        self,
        step: Theorem | Construction,
        inputs: frozendict[GeoObject, GeoObject],
        score: float | None = None,
        phase: int | None = None,
        out_names: dict[str, float] | None = None,
    ):
        self.step = step

        # TODO: Find a cleaner way to get rid of substitutions in `inputs` that are `Construction`s.
        self.inputs = {
            key: value
            for (key, value) in inputs.items()
            if not isinstance(key, ConstructionObject) and not isinstance(key, EquationObject)
        }

        self.score = -math.inf if score is None else score
        self.phase = 0 if phase is None else phase
        self.construction_penalties = out_names

    def is_ready(self) -> bool:
        return self.phase == 2

    def step_score(self, checker: ProofChecker, *, verb=False) -> float:
        """
        Computes the full score of the step.
        """
        if isinstance(self.step, Construction):
            # There are few constructions, and I can give them scores by hand.
            return construction_penalty(self.step, checker) + 5  # I'd rather add theorems than constructions.
        assert isinstance(self.step, Theorem)

        direct_construction_count = len(self.step.result_objects)
        pred_score = theorem_score(self.step)
        constructions = [c.substitute(self.inputs) for c in cached_constructions(self.step)]
        indirect_constructions = [c for c in constructions if not checker.geometry_tracker.contains_object(c)]
        self.construction_penalties = {
            c.name: construction_penalty(c, checker)
            for c in indirect_constructions
            if construction_penalty(c, checker) > 0
        }
        if verb:
            print(f'{direct_construction_count=} {pred_score=} {self.construction_penalties=}')
        return (
            direct_construction_count * CONSTRUCTION_PENALTY
            + sum(self.construction_penalties.values())
            + pred_score
            - self.step.rank * 10
        )

    def update_score(self, checker: ProofChecker):
        """
        Updates the score of the step.
        """
        if self.phase == 0:
            return
        elif self.phase == 2:
            self.score = self.step_score(checker)

    def refine_score(self, checker: ProofChecker):
        """
        Improves the score of the StepSuggestion.
        """
        if self.phase == 0:
            self.score = self.step_score(checker) + math.log(random.random())
            self.phase = 2
        else:
            raise GeometryError(f'StepSuggestion::refine_step called on step {self}!')

    def to_step(self, checker: ProofChecker, all_names: set[str]) -> TheoremStep | ObjDefineStep:
        """
        Converts the step suggestion to an actionable step.
        """
        if self.phase != 2:
            raise GeometryError(
                f'Attempted to convert step suggestion {self} to a step without fully refining the score!'
            )

        if isinstance(self.step, Construction):
            return ObjDefineStep(self.step(*[self.inputs[sig] for sig in self.step.signature]))
        elif isinstance(self.step, Theorem):
            res_objects = [GeoObject(gen_name(all_names), res.type) for res in self.step.result_objects]
            full_sub = self.inputs | {out: res for out, res in zip(self.step.result_objects, res_objects)}
            res_predicates = [pred.substitute(full_sub) for pred in self.step.result_predicates]

        return TheoremStep(
            self.step.name, [self.inputs[sig] for sig in self.step.signature], res_objects, res_predicates
        )

    def __hash__(self) -> int:
        return hash((self.step, self.inputs))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StepSuggestion):
            return False
        return self.step == other.step and self.inputs == other.inputs

    def __repr__(self) -> str:
        return f'Step({self.step.name}, {self.inputs}, phase={self.phase}, score={self.score})'

    def __lt__(self, other: 'StepSuggestion') -> bool:
        return self.score < other.score
