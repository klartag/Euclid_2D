import heapq
from typing import Optional

from ..embeddings.embedded_predicate_value import EmbeddedPredicateValue
from ..embeddings.undefined_embedding_error import UndefinedEmbeddingError
from ..predicates.predicate_factory import predicate_from_args
from ..theorem import Theorem
from ..embeddings import Embedding
from ..proof_checker_utils import (
    get_linear_eqn_factors,
    get_log_eqn_factors,
    unpack_predicate_full,
    unpack_predicate_minimal,
)
from ..errors import GeometryError, IllegalObjectError, ProofCheckError
from ..geometry_objects.geo_type import GeoType, R_EQN_TYPES, Signature
from ..geometry_objects.atom import Atom
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.literal import ONE, Literal
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.construction_object import Construction, ConstructionObject
from ..predicates.predicate import Predicate
from ..predicates.implementations.macro_predicate import MacroPredicate
from ..proof.geometry_problem import GeometryProblem
from ..union_find.union_find import UnionFind

from .congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker

from .linear_algebra_tracker.linear_algebra_tracker import LinearAlgebraTracker
from .linear_algebra_tracker.linear_expression import LinearExpression

NUMERIC_PRECISION = 1e-3
"""
"""


def involved_objects(
    obj: Construction | GeoObject | Predicate | Theorem, res: set[GeoObject] | None = None
) -> set[GeoObject]:
    """
    Gets all the objects involved in the construction of the given object.
    For center(Circle(a,b,c)), this should return {center(Circle(a,b,c)), Circle(a,b,c), a, b, c}.
    """
    if res is None:
        res = set()
    if obj in res:
        return res

    match obj:
        case Construction():
            for inp in obj.signature:
                involved_objects(inp, res)
            for pred in obj.required_predicates:
                involved_objects(pred, res)
        case Theorem():
            for inp in obj.signature:
                involved_objects(inp, res)
            for pred in obj.required_predicates:
                involved_objects(pred, res)
        case Predicate():
            for sub_pred in unpack_predicate_minimal(obj):
                if sub_pred.name == 'equals' and sub_pred.components[0].type in (
                    GeoType.LITERAL,
                    GeoType.SCALAR,
                    GeoType.ANGLE,
                ):
                    factors = get_linear_eqn_factors(sub_pred)
                    if factors is None:
                        factors = get_log_eqn_factors(sub_pred)
                    assert factors is not None
                    for factor in factors:
                        involved_objects(factor, res)

                for comp in sub_pred.components:
                    involved_objects(comp, res)
        case EquationObject():
            factors = obj.as_linear_equation()
            if factors is None:
                factors = obj.as_log_equation()
            assert factors is not None

            for factor in factors:
                involved_objects(factor, res)
        case ConstructionObject():
            res.add(obj)
            if isinstance(obj, ConstructionObject):
                for comp in obj.components:
                    involved_objects(comp, res)
        case Atom():
            res.add(obj)
        case Literal():
            pass

    return res


class GeometryTracker:
    """
    A class that checks that a proof is valid.
    """

    signature: Signature
    _predicates: set[Predicate]
    """All predicates known to be true."""
    _asserted_predicates: set[Predicate]
    """The predicates added by assert steps. These are used as markers, and are not substituted by other actions."""
    _linear_algebra: LinearAlgebraTracker
    """Tracks equalities between linear combinations of values."""
    equality_tracker: CongruenceClosureTracker
    """Tracks equalities of Geometry Objects up to a relation with congruence closure."""
    embedding_tracker: Optional[Embedding]
    """Tracks 2D embeddings of the geometric configurations."""

    def __init__(self):
        self.signature = {}

        self._predicates = set()
        self._asserted_predicates = set()

        self._linear_algebra = LinearAlgebraTracker()
        self.equality_tracker = CongruenceClosureTracker()
        self.embedding_tracker = None

        self.equality_tracker.normalize(ONE)

    def load_embedding(self, problem: GeometryProblem):
        """
        Loads the data of the known point embeddings.
        """
        if problem.embedding is not None:
            self.embedding_tracker = problem.embedding.shallow_copy()

    def all_predicates(self) -> set[Predicate]:
        """
        Returns all predicates known by the checker."""
        return self._predicates | self._asserted_predicates

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

        a, b, c = angle.components
        if a != c:
            rev_angle = self.equality_tracker.normalize(ConstructionObject.from_args('angle', (c, b, a)))
            if self.embedding_tracker is not None:
                self._linear_algebra.add_relation_mod(
                    LinearExpression({angle: 1, rev_angle: 1}), 0, 360, self.embedding_tracker, None
                )

    def process_object(self, obj: GeoObject):
        """
        Adds all conclusions derived from a legal object.
        This function is called only when the object is deemed legal and should be added.
        """
        if obj in self._processed_objects:
            return
        if obj.name == '0':
            return
        self._processed_objects.add(obj)

        for equiv in list(self.equality_tracker.get_equivalences(obj)):
            self.process_object(equiv)

        if isinstance(obj, ConstructionObject):
            # We add the requirements, since objects in the assumptions might not have all requirements.
            for req in obj.requirements():
                self.add_predicate(req, f'Requirement of {obj}')
            for comp in obj.components:
                self.process_object(self.equality_tracker.normalize(comp))
            for pred in obj.conclusions():
                self.add_predicate(pred, f'conclusion of {obj}')

            for req_preds, res_preds in obj.possible_conclusions():
                if all(self.contains_predicate(pred, can_add=False) for pred in req_preds):
                    for pred in res_preds:
                        self.add_predicate(pred, f'Possible conclusion of {obj}')

        if isinstance(obj, EquationObject):
            for comp in involved_objects(obj):
                self.process_object(self.equality_tracker.normalize(comp))

        match obj.type:
            case GeoType.ANGLE:
                self.process_angle(obj)

        if (
            self.embedding_tracker is not None
            and isinstance(obj, ConstructionObject)
            and obj.name not in self.embedding_tracker
        ):
            try:
                embedded_construction_object_options = self.embedding_tracker.evaluate_construction_object(obj)
                if len(embedded_construction_object_options) == 1:
                    self.embedding_tracker[obj.name] = embedded_construction_object_options[0]
            except UndefinedEmbeddingError:
                pass

    def add_equal_angle(self, pred: Predicate, mod: int | None):
        """
        Handles an angle equality predicate.
        @param angle: A predicate stating that some linear combination of angles is 0.
        @param mod: The modulus under which the equality is valid.
        """
        if self.embedding_tracker is None: return
        
        factors = get_linear_eqn_factors(pred)
        if factors is None:
            raise GeometryError(f'Failed to convert equation {pred.to_language_format()} to a linear equation!')
        if mod is not None:
            for v in factors.values():
                if abs(v - round(v)) > 1e-3:
                    raise ProofCheckError(f'In predicate {pred}, recived fractional value!')

        if mod is None:
            self._linear_algebra.add_relation(LinearExpression(factors), 0, self.embedding_tracker, pred)
        else:
            self._linear_algebra.add_relation_mod(LinearExpression(factors), 0, mod, self.embedding_tracker, pred)

    def add_equal_scalar(self, pred: Predicate):
        """
        Handles an equality of scalars.
        """
        # Adding the equation as a normal equation.
        if self.embedding_tracker is None: return
        factors = get_linear_eqn_factors(pred)
        if factors is not None:
            self._linear_algebra.add_relation(LinearExpression(factors), 0, self.embedding_tracker, pred)

        # Adding the equation as a log equation.
        # We do this by default only to equations that are not normal equations, since logs are also non-zero.
        else:
            log_factors = get_log_eqn_factors(pred)
            if log_factors is not None:
                for factor in log_factors:
                    self.equality_tracker.normalize(factor)
                self._linear_algebra.add_relation(LinearExpression(log_factors), 0, self.embedding_tracker, pred)

    def _add_equal_objects_nonrecursive(self, a: GeoObject, b: GeoObject):
        """
        Sets the object `a` to be equal to the object `b`.

        This has to be tracked in several places:

        1. TODO: Rethink and possibly fix bugs (I think that by luck the bug is guaranteed not to happen).
            There are objects that haven't been processed.
            If one of the equivalent objects is processed and the other is not,
            then we mark all equivalent objects as processed.
            Note, however, that we do not process them, and that it is in general illegal
            to have predicates (such as equality) describing objects that were not processed,
            so this doesn't cause a problem, but this should just be eliminated.

        2. Mark the object as equals in the union-find tree.

        3. Mark the objects as equal in the linear algebra trackers.
        """
        if a == b:
            return
        assert a > b, f'_add_equal_objects_nonrecursive got illegal objects: {a} {b}'

        self._objects[a]
        self._objects[b]

        # Step 1.
        if b in self._processed_objects and a not in self._processed_objects:
            for obj in self._objects.get_equivalences(a):
                self._processed_objects.add(obj)
        elif a in self._processed_objects and b not in self._processed_objects:
            for obj in self._objects.get_equivalences(b):
                self._processed_objects.add(obj)

        # Step 2.
        self._objects[a] = b

        assert (b in self._processed_objects) == (a in self._processed_objects)

        # Step 3.
        # Adding the equality relation to any tracker where at least one object appears.
        # Since one of the old objects will no longer be accessible, we only have to add an equality relation
        # If the old object was tracked in some form.
        if self._linear_algebra.contains_key(a):
            self._linear_algebra.add_relation(LinearExpression({a: 1, b: -1}), 0, self.embedding_tracker)

    def add_equal_object(self, g1: GeoObject, g2: GeoObject):
        """
        Adds a generic equality of objects.
        The objects are merged in the proof-checker's union-find tree.
        """

        substitutions = {}

        # We first find the canonical representative of each object.
        g1 = self._objects[g1]
        g2 = self._objects[g2]

        if g1 == g2:
            return

        if g1 < g2:
            g1, g2 = g2, g1
        # The equality queue is a priority queue, containing objects that were
        # representatives before the equality operation, but are no longer representatives.
        historical_equality_queue = {g1}
        equality_queue = [g1]

        self._add_equal_objects_nonrecursive(g1, g2)
        substitutions[g1] = g2

        while len(equality_queue) > 0:
            a = heapq.heappop(equality_queue)
            a_rep = self._objects[a]

            assert a != a_rep

            # The object list may change during iteration, which requires another check.
            for obj in list(self._objects.all_objects()):
                if isinstance(obj, ConstructionObject) and a in obj.components:
                    # Checking if the canonical object exists.
                    rep = self._objects[obj]
                    substituted_rep = self.equality_tracker.normalize(
                        ConstructionObject.from_args(
                            obj.constructor.name, tuple(self._objects[comp] for comp in obj.components)
                        )
                    )

                    # The substituted object is already known to exist and be in the correct equivalence class.
                    if rep == substituted_rep:
                        continue
                    if rep < substituted_rep:
                        rep, substituted_rep = substituted_rep, rep

                    self._add_equal_objects_nonrecursive(rep, substituted_rep)
                    substitutions[rep] = substituted_rep
                    if substituted_rep not in historical_equality_queue:
                        heapq.heappush(equality_queue, rep)
                        historical_equality_queue.add(rep)

        # Using Predicate::substitute is terrible here although it is the correct thing,
        # since it is a recursive call over all nested components
        new_predicates = set()
        for pred in self._predicates:
            if any(obj in substitutions for obj in pred.components):
                new_predicates.add(
                    predicate_from_args(pred.name, tuple(substitutions.get(obj, obj) for obj in pred.components))
                )
            else:
                new_predicates.add(pred)

        self._predicates = new_predicates

    def add_predicate(self, pred: Predicate, reason: str):  # TODO: Why is `reason` unused?
        """
        Adds the given predicate to the list of known predicates.
        @param pred: A predicate to add.
        @param config: Whether all construction objects specified by the predicate are known to exist.
        @param reason: The context in which the predicate was added.
        """
        if pred not in self._predicates:
            pred = self.get_predicate(pred, can_add=True)
            for sub_pred in unpack_predicate_full(pred):
                self.add_unpacked_predicate(sub_pred, reason=f'unpack of {pred}')

    def add_unpacked_predicate(self, pred: Predicate, reason=''):
        """
        Adds predicates to the proof checker without attempting to unpack them first (See Predicate::unpack).

        Parameters:
        * `pred`: A predicate to add.
        * `config`: A configuration specifying the desired behavior of the checker (See `StepConfig`).
                    In this case, it only specifies if the objects referred to in the predicate are known to exist,
                    or if the conditions for their existence should be checked and an exception should be raised
                    when they are not satisfied.
        * `reason`: The reason for adding the predicate. Is also only used for debug purposes.

        The function has three steps:
        1. Normalizing the predicate to use only the canonical representatives of objects (See `Self::get_predicate` or `Self::get_object`).
        2. Macro predicates (See `MacroPredicate`) can have possible conclusions (Which is a terrible system and should be deprecated).
            If the predicate is a macro predicate, we attempt to add the possible conclusions.
        3. Dispatching the predicate to the linear algebra trackers if it is an equation, and directly adding it otherwise.
        """
        # Optimization: If the predicate is already known, be don't have to add it.
        if pred in self._predicates:
            return

        # The predicate could refer to objects that were merged, so we need to update the predicate to use the newer objects.
        pred = self.get_predicate(pred, can_add=True)
        if pred in self._predicates:
            return
        # if self.contains_predicate(pred, can_add=False):
        #     return

        # Macro predicates might have possible conclusions, that also have to be added.
        if isinstance(pred, MacroPredicate):
            for req_preds, conc_preds in pred.possible_conclusions():
                if all(self.contains_predicate(req_pred, can_add=False) for req_pred in req_preds):
                    for conc_pred in conc_preds:
                        self.add_predicate(
                            conc_pred,
                            'Possible conclusion of {pred}',
                        )

        if self.contains_predicate(pred, can_add=False):
            return

        # After this line, the predicate refers to legal objects, so it is trusted.
        # print(f'Adding unpacked predicate {pred.to_language_format()} by {reason}')
        match pred.name:
            case 'equals':
                # There are several behaviors here:
                # - Equality between general objects.
                # - Equality between scalars / equations. In this case, we just tell the linear algebra tracker what to do.
                assert len(pred.components) == 2

                match (pred.components[0].type, pred.components[1].type):
                    case (GeoType.SCALAR, _) | (_, GeoType.SCALAR):
                        # Handling a scalar equation.
                        self.add_equal_scalar(pred)
                    case (GeoType.ANGLE, _) | (_, GeoType.ANGLE):
                        # Handling an angle equation with no modulus.
                        self.add_equal_angle(pred, None)
                    case (GeoType.ORIENTATION, _) | (_, GeoType.ORIENTATION):
                        pass
                    case _:
                        # Generic object equality.
                        a, b = pred.components
                        self.add_equal_object(a, b)
            case 'equals_mod_360':
                self.add_equal_angle(pred, 360)
            case 'not_equals' | 'not_equals_mod_360':
                pass
                # raise NotImplementedError("The Geometry Tracker does not track not_equals predicates.")
        if pred.name != 'exists':
            for obj in pred.involved_objects():
                predicate = predicate_from_args('exists', (obj,))
                self.add_predicate(predicate, 'Marking an object involve in some proved predicate as existing')

        # We add the predicate to self anyway.
        self._predicates.add(pred)

    def get_predicate(self, pred: Predicate, *, can_add: bool) -> Predicate:
        """
        Gets the predicate, substituted to use the canonical representative (See Self::get_object) of each object.
        For example, if it is known that `A == B` and `C == D`,
        `get_predicate(between(A, B, D))` would return `between(A, A, C)`.
        @pred: Some predicate.
        @return: The predicate, with the objects substituted with their canonical representatives.

        The function first attempts to add all objects to the checker before getting the predicate
        to avoid cases where conclusions of the constructions contain equalities that change the
        canonical representative of the original predicate.
        """
        for obj in pred.components:
            self.equality_tracker.normalize(obj)

        subs = {obj: self.equality_tracker.normalize(obj) for obj in pred.components}

        # if config.add_obj:
        #     print(f'get_predicate: {pred} {subs} {pred.substitute(subs)}')

        return pred.substitute(subs)

    def contains_object(self, obj: GeoObject) -> bool:
        """
        Checks if the ProofChecker has already processed the object.

        Parameters:
        * `obj`: A geometric object.
        """
        return obj in self._processed_objects

    def contains_predicate(self, pred: Predicate, *, can_add: bool, old_method: bool = False) -> bool:
        """
        Checks if the given predicate is contained in the proof checker.

        Parameters:
        * `pred`: A predicate.
        * `config`: The configuration to use when checking if objects exist.

        This operation has several steps.

        1. Unpacking the predicate.
            Predicates are sometimes equivalent to the intersection of some other predicates,
            as in between(A, B, C, D) == between(A, B, C) && between(B, C, D),
            or in square(A, B, C, D).
            In this case, we have to find the minimal set of predicates such that if all predicates in
            the set are true then the predicate is true, and check them.

        2. Normalizing the predicate.
            The predicate might refer to objects instead of their canonical representatives
            (See Self::get_object), but predicates are stored internally using the canonical representatives.
            When checking if it is contained, we have to change it to use the canonical representatives of the objects in it.

        3. Checking in the appropriate tracker if the predicate is known to be true,
            or if the predicate is trivial.
            Here, if the predicate is an equation (`equals`, `equals_mod_360`)
            it is dispatched to the appropriate linear algebra tracker.
            Otherwise, we just check if it is contained in the set of predicates.
        """

        # Optimization: The predicate was added directly to the list of predicates,
        # and we can return True without more expensive checks.
        if pred in self._predicates:
            return True

        # If the predicate does not appear in the unpacking, then it is a macro, and it is both sufficient and necessary for all
        # unpacked predicates to be contained.
        unpacked = unpack_predicate_minimal(pred)
        if pred not in unpacked:
            return all(self.contains_predicate(sub_pred, can_add=can_add) for sub_pred in unpacked)

        # Preprocessing all the object and updating the predicate to use the representative objects.
        # Since this is a query, we do not trust that all objects in the predicate are legal.
        try:
            pred = self.get_predicate(pred, can_add=can_add)
        except IllegalObjectError:
            return False

        # Equality and equality mod predicates are tracked by the linear algebra trackers.
        match pred.name:
            case 'equals':
                a, b = pred.components
                typ = a.type if a.type != GeoType.LITERAL else b.type
                if typ in R_EQN_TYPES:
                    if self.embedding_tracker is None:
                        return False
                    factors = get_linear_eqn_factors(pred)
                    if (
                        factors is not None
                        and self._linear_algebra.try_evaluate(LinearExpression(factors), self.embedding_tracker)
                        == 0
                    ):
                        return True
                    factors = get_log_eqn_factors(pred)
                    return (
                        factors is not None
                        and self._linear_algebra.try_evaluate(LinearExpression(factors), self.embedding_tracker)
                        == 0
                    )

                if typ == GeoType.ORIENTATION:
                    if self.embedding_tracker is None:
                        return False
                    factors = get_linear_eqn_factors(pred)
                    return (
                        factors is not None
                        and self._linear_algebra.try_evaluate(LinearExpression(factors), self.embedding_tracker)
                        == 0
                    )

                return self.equality_tracker.are_congruent(a, b)
            case 'equals_mod_360':
                if self.embedding_tracker is None:
                        return False
                factors = get_linear_eqn_factors(pred)
                if factors is None:
                    return False
                if self.embedding_tracker is None: return False
                result = self._linear_algebra.try_evaluate(LinearExpression(factors), self.embedding_tracker)
                return result is not None and result % 360 == 0

            case 'not_equals' | 'not_equals_mod_360':
                if self.embedding_tracker is None: return False
                return self.embedding_tracker.evaluate_predicate(pred) == EmbeddedPredicateValue.Correct
            case 'between' | 'collinear':
                if pred.components[0] == pred.components[1] or pred.components[2] == pred.components[1]:
                    return True

        return pred in self._predicates

    def clone(self) -> 'GeometryTracker':
        """
        Returns a copy of the geometry tracker.
        """
        res = GeometryTracker()
        res.signature = self.signature.copy()
        res._predicates = set(self._predicates)
        res._asserted_predicates = set(self._asserted_predicates)
        res._linear_algebra = self._linear_algebra.clone()
        res.equality_tracker = self.equality_tracker.clone()
        if self.embedding_tracker is not None:
            res.embedding_tracker = self.embedding_tracker.shallow_copy()
        return res

    def load_assumptions(self, problem: GeometryProblem):
        """
        Loads all assumption data from the problem into the checker.
        The assumption data includes:
        1. Objects in the problem description.
        2. Predicates on these objects.
        3. Embeddings of the objects into R^2, if they are present.
        """
        self.load_embedding(problem)
        
        assert problem.statement is not None

        # Adding the objects defined by the proof.
        for obj in problem.statement.assumption_objects.values():
            self.equality_tracker.normalize(obj)

        # Adding the assumptions of the proof.
        for pred in problem.statement.assumption_predicates:
            self.add_predicate(pred, 'Assumption predicate')

        for pred in problem.statement.auxiliary_predicates:
            self.add_predicate(pred, 'Auxiliary predicate')
