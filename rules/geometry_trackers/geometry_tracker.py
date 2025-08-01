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
from ..rust_code.rust_sparse_linear import BaseSolver
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
from ..union_find import UnionFind

from .linear_algebra_tracker import LinearAlgebraTracker

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
    _objects: UnionFind[GeoObject]
    """All legal objects currently used by the proof."""
    _processed_objects: set[GeoObject]
    """All legal objects that can be used by the proof, but not yet. 
    They are logged, but their conclusions haven't been added."""
    _predicates: set[Predicate]
    """All predicates known to be true."""
    _asserted_predicates: set[Predicate]
    """The predicates added by assert steps. These are used as markers, and are not substituted by other actions."""
    _linear_algebra: LinearAlgebraTracker

    embedding_tracker: Optional[Embedding]
    """Tracks 2D embeddings of the geometric configurations."""

    def __init__(self):
        self.signature = {}
        self._objects = UnionFind()
        self._processed_objects = set()
        self._drawn_objects = set()

        self._predicates = set()
        self._asserted_predicates = set()
        self.embedding_tracker = None

        self.get_object(ONE, can_add=True)

        self._linear_algebra = LinearAlgebraTracker()

    def load_embedding(self, problem: GeometryProblem):
        """
        Loads the data of the known point embeddings.
        """
        if problem.embedding is not None:
            self.embedding_tracker = problem.embedding.shallow_copy()

    def get_object(self, obj: GeoObject, *, can_add: bool) -> GeoObject:
        """
        Gets the canonical representative object in the proof checker associated with the given object by the equality system (This is important).
        This function also handles the processing of construction objects, which is bad and should be refactored (TODO).

        The proof checker tracks equalities of objects, such as `A == B`.
        In this case, it has no need of predicates referring to `B`,
        and converts all queries and operation to operations referring to `A`.
        In addition, the equalities are propagated through constructions, so that `A == B` implies `Line(A, X) == Line(B, X)`.

        Before any `return` that could return a construction object,
        the function processes it if it should be processed, but hasn't been processed yet.

        The function:

        1. Checks if the object is present in the UnionFind tree.
            This works for all processed objects, but might not work for constructions that weren't processed
            (In the example above, prehaps `Line(A, X)` is processed, but `Line(B, X)` isn't).

        2. If the object is a construction object, converts all its arguments to the canonical representatives of their arguments.
            The equality system maintains that for any construction object, the result of substituting all its arguments
            to their canonical representative must also be present in the UnionFind tree even if that is not the canonical representative,
            to ensure that this step works.
            In the example above, if we have `Line(B, X) == l` where `l` is the canonical representative,
            then `Line(A, X)` will also be in the UnionFind tree.

        3. If the object is an equation object, then we just substiute the components,
            since linear algebra is not tracked by the equality system.

        Now we perform two more actions apart from the stated purpose: (TODO: Refactor)
        4. We validate that for a construction object, all requirements are known to be true.
        5. We store new contruction objects in the UnionFind tree,
            but not in the `self._processed_objects` set, to make finding them in the future easier.
            We do this only if they should be added, or if we have checked that their requirements are satisfied.
        """
        # If we already know the object, we just add it.
        if obj in self._objects:
            # If the object was known, but not processed, we process it.
            if can_add and obj not in self._processed_objects:
                self.process_object(self._objects[obj])
            res = self._objects[obj]
            assert res <= obj, f'ProofChecker::get_object increased the value: {obj} => {res}'
            return res

        if isinstance(obj, Atom):
            self.signature[obj.name] = obj.type

        # If the object is a construct, we substitute the components.
        # A construction object must always satisfy that the substitution of its components to the canonical components
        # is also in the system.
        if isinstance(obj, ConstructionObject):
            res = obj.substitute({comp: self.get_object(comp, can_add=can_add) for comp in obj.components})
            if res != obj:
                # print(f'Substituted {obj} => {res}')
                res = self.get_object(res, can_add=can_add)
                # Logging the object and its substituted version for future reference.
                assert res <= obj, f'Illegal substitution: {obj} => {res}'

                # When we trust the object and don't check, we can't store references to it.
                if can_add:
                    self.add_equal_object(obj, res)

                # The new object might already be known, or might have non-trivial equalities.
                return self.get_object(res, can_add=can_add)

        # If the object is an equation, we substitute the components.
        if isinstance(obj, EquationObject):
            return EquationObject(
                self.get_object(obj.left, can_add=can_add), self.get_object(obj.right, can_add=can_add), obj.op
            )

        # We now have an new unknown object that shouldn't be substituted.
        if isinstance(obj, ConstructionObject) and not can_add:
            for pred in obj.requirements():
                if not self.contains_predicate(pred, can_add=False):
                    raise IllegalObjectError(
                        f'Attempted to add the construction object {obj} without the ' f'requirement {pred}!'
                    )

        # Objects are stored as legal only if:
        # 1. They are untrusted, but have been checked.
        # 2. They should be added.
        if can_add:
            self._objects[obj]
            self.process_object(obj)

        return obj

    def unique_objects(self) -> set[GeoObject]:
        """
        Returns an iterator over the set of canonical representative objects, not counting equal objects twice.
        """
        return set(self._objects.get_representatives()) & self._processed_objects

    def all_objects(self) -> set[GeoObject]:
        """
        Returns an iterator over all tracked objects.
        """
        return set(self._processed_objects)

    def represented_objects(self, obj) -> set[GeoObject]:
        """
        Returns all objects represented by the given object.
        """
        assert obj in self._objects
        rep = self._objects[obj]
        return self._objects.get_equivalences(rep) & self._processed_objects

    def all_predicates(self) -> set[Predicate]:
        """
        Returns all predicates known by the checker."""
        return self._predicates | self._asserted_predicates

    def trackers(self) -> list[BaseSolver]:
        """
        Returns the list of trackers of the proof checker.
        """
        return [
            self._linear_algebra.bool_equations,
            self._linear_algebra.mod_360_equations,
            self._linear_algebra.real_equations,
        ]

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

        assert angle in self._processed_objects and angle in self._objects

        a, b, c = angle.components
        if a != c:
            rev_angle = self.get_object(ConstructionObject.from_args('angle', (c, b, a)), can_add=True)
            assert rev_angle in self._processed_objects and rev_angle in self._objects
            self._linear_algebra.real_equations.add_relation({angle: 1, rev_angle: 1})
            self._linear_algebra.mod_360_equations.add_relation({angle: 1, rev_angle: 1})

    def process_orientation(self, ori: GeoObject):
        """
        Adds automatic theorems to an orientation.
        The single theorem currenlt added is:
        * `orientation(A, B, C) != orientation(C, B, A)`

        Parameters:
        * `ori`: An orientation to add theorems to.
        """
        if not isinstance(ori, ConstructionObject) or ori.constructor.name != 'orientation':
            return

        a, b, c = ori.components
        self.add_predicate(predicate_from_args('not_collinear', (a, b, c)), 'Since they have an orientation.')

        rev = self.get_object(ConstructionObject.from_args('orientation', ori.components[::-1]), can_add=True)
        assert rev in self._processed_objects and rev in self._objects

        if ori != rev:
            self._linear_algebra.bool_equations.add_relation({ori: True, rev: True, ONE: True})
        else:
            # We get a contradiction, and properly add it.
            self._linear_algebra.bool_equations.add_relation({ONE: True})

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

        for equiv in list(self._objects.get_equivalences(obj)):
            self.process_object(equiv)

        if isinstance(obj, ConstructionObject):
            # We add the requirements, since objects in the assumptions might not have all requirements.
            for req in obj.requirements():
                self.add_predicate(req, f'Requirement of {obj}')
            for comp in obj.components:
                self.process_object(self.get_object(comp, can_add=True))
            for pred in obj.conclusions():
                self.add_predicate(pred, f'conclusion of {obj}')

            for req_preds, res_preds in obj.possible_conclusions():
                if all(self.contains_predicate(pred, can_add=False) for pred in req_preds):
                    for pred in res_preds:
                        self.add_predicate(pred, f'Possible conclusion of {obj}')

        if isinstance(obj, EquationObject):
            for comp in involved_objects(obj):
                self.process_object(self.get_object(comp, can_add=True))

        match obj.type:
            case GeoType.ANGLE:
                self.process_angle(obj)
            case GeoType.ORIENTATION:
                self.process_orientation(obj)

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
        factors = get_linear_eqn_factors(pred)
        if factors is None:
            raise GeometryError(f'Failed to convert equation {pred.to_language_format()} to a linear equation!')
        if mod is not None:
            for v in factors.values():
                if abs(v - round(v)) > 1e-3:
                    raise ProofCheckError(f'In predicate {pred}, recived fractional value!')

        match mod:
            case None:
                self._linear_algebra.real_equations.add_relation(factors)
                self._linear_algebra.mod_360_equations.add_relation(factors)
            case 360:
                self._linear_algebra.mod_360_equations.add_relation(factors)
            case _:
                raise NotImplementedError(f'Equality mod {mod} in predicate {pred} is not implemented!')

    def add_equal_scalar(self, pred: Predicate):
        """
        Handles an equality of scalars.
        """
        # Adding the equation as a normal equation.
        if (factors := get_linear_eqn_factors(pred)) is not None:
            self._linear_algebra.real_equations.add_relation(factors)

        # Adding the equation as a log equation.
        # We do this by default only to equations that are not normal equations, since logs are also non-zero.
        elif (log_factors := get_log_eqn_factors(pred)) is not None:
            for factor in log_factors:
                self.get_object(factor, can_add=True)
            self._linear_algebra.real_equations.add_relation(log_factors)

    def add_equal_bool(self, pred: Predicate):
        """
        Handles an equality of orientations.
        """
        if (factors := get_linear_eqn_factors(pred)) is not None:
            self._linear_algebra.bool_equations.add_relation(factors)

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
        for tracker in self.trackers():
            # Note: Since we know that a is set to become b, we don't need to add the relation if a is nonexistent.
            if tracker.contains(a):
                tracker.add_relation({a: 1, b: -1})

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
                    substituted_rep = self.get_object(
                        ConstructionObject.from_args(
                            obj.constructor.name, tuple(self._objects[comp] for comp in obj.components)
                        ),
                        can_add=True,
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
                        self.add_equal_bool(pred)
                    case _:
                        # Generic object equality.
                        a, b = pred.components
                        self.add_equal_object(a, b)
            case 'equals_mod_360':
                self.add_equal_angle(pred, 360)
            case 'not_equals' | 'not_equals_mod_360':
                raise NotImplementedError("The Geometry Tracker does not track not_equals predicates.")
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
            self.get_object(obj, can_add=can_add)

        subs = {obj: self.get_object(obj, can_add=can_add) for obj in pred.components}

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

    def contains_predicate(self, pred: Predicate, *, can_add: bool) -> bool:
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
        if pred not in (unpacked := unpack_predicate_minimal(pred)):
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
                    if (
                        factors := get_linear_eqn_factors(pred)
                    ) is not None and self._linear_algebra.real_equations.contains_relation(factors):
                        return True
                    if (
                        factors := get_log_eqn_factors(pred)
                    ) is not None and self._linear_algebra.real_equations.contains_relation(factors):
                        return True
                    return False

                if typ == GeoType.ORIENTATION:
                    return (
                        factors := get_linear_eqn_factors(pred)
                    ) is not None and self._linear_algebra.bool_equations.contains_relation(factors)

                return self.get_object(a, can_add=can_add) == self.get_object(b, can_add=can_add)
            case 'equals_mod_360':
                return (
                    factors := get_linear_eqn_factors(pred)
                ) is not None and self._linear_algebra.mod_360_equations.contains_relation(factors)
            case 'not_equals' | 'not_equals_mod_360':
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
        res._objects = self._objects.shallow_copy()
        res._processed_objects = set(self._processed_objects)
        res._predicates = set(self._predicates)
        res._asserted_predicates = set(self._asserted_predicates)
        res._linear_algebra = self._linear_algebra.clone()
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
        # Adding the objects defined by the proof.
        for obj in problem.statement.assumption_objects.values():
            self.get_object(obj, can_add=True)

        # Adding the assumptions of the proof.
        for pred in problem.statement.assumption_predicates:
            self.add_predicate(pred, 'Assumption predicate')

        for pred in problem.statement.auxiliary_predicates:
            self.add_predicate(pred, 'Auxiliary predicate')
