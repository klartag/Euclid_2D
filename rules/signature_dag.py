import abc
import functools
import itertools
from typing import Sequence, TypeVar
import warnings

from frozendict import frozendict

from rules.geometry_objects.atom import Atom

from .predicates.predicate_factory import predicate_from_args

from .geometry_trackers.geometry_tracker import GeometryTracker, involved_objects
from .geometry_objects.construction_object import Construction, ConstructionObject
from .geometry_objects.geo_object import ONE, ZERO, GeoObject
from .geometry_objects.equation_object import EquationObject
from .proof_checker_utils import (
    KNOWN_KEYS,
    TRUST_NO_ADD_CFG,
    get_eqn_key,
    get_linear_eqn_factors,
    get_log_eqn_factors,
    unpack_predicate_full,
    unpack_predicate_minimal,
)
from .rule_utils import ANGLE, CIRCLE, EQN_TYPES, LINE, LITERAL, ORIENTATION, POINT, SCALAR, GeometryError
from .theorem import Theorem
from .union_find import UnionFind
from .rust_code.rust_match import RustMatch
from .predicates.predicate import Predicate


MAX_INTERSECTION_PATTERN_MATCHES = 100_000
"""A maximal number of possible matches. Supposed to prevent theorems with an excessive number of 
objects from freezing the whole program with no option to unfreeze it, but currently only used to warn."""


@functools.cache
def extended_type(obj: GeoObject) -> str:
    """
    The type of the object, with more metadata on the construction:
    The extended type of `line_angle(l)` would be `line_angle` instead of the more generic `Angle`.
    This is used to search for fewer combinations in Equation and Nonzero patterns.

    Parameters:
    * `obj`: A geometric object.

    Return:

    Some metadata on the object's type and construction.
    """
    if isinstance(obj, ConstructionObject):
        return obj.constructor.name
    else:
        return obj.type


TYPE_NAMES = {POINT: 'P', LINE: 'L', CIRCLE: 'C', ORIENTATION: 'O', ANGLE: 'A', SCALAR: 'S', LITERAL: 'LIT_'}

T = TypeVar('T', GeoObject, Predicate)


def normalize(
    obj: T, keys: dict[int, int], names: set[str] | None = None, subs: dict[GeoObject, GeoObject] | None = None
) -> T:
    """
    Converts the names of the components of the object to canonical names,
    and returns the normalized object and the dictionary mapping old keys to new keys.

    Parameters:
    * `obj`: The object to normalize. Could be a GeoObject, which will be converted to a semi-canonical form
             `(Atom('A', 'Point')` will be converted to `Atom('Point_0', 'Point')`).
    * `keys`: A mapping from all keys in the resulting object to the original keys, ro be used in a `RekeyPattern`.
              When converting `Line(A, B)` to `Line(Point_0, Point_1)`, this will map the key of `Point_0` to the key of `A`,
              the key of `Point_1` to the key of `B`, and the key of `Line(Point_0, Point_1)` to the key of `Line(A, B)`.
    * `names`: The names we have added, so that we don't add the same name twice.
    * `subs`: A map from the objects we normalized to their normalized versions.

    Return:

    A semi-canonical version of the object.
    """
    if names is None:
        names = set()
    if subs is None:
        subs = {}
    if isinstance(obj, EquationObject):
        return EquationObject(normalize(obj.left, keys, names, subs), normalize(obj.right, keys, names, subs), obj.op)  # type: ignore
    elif isinstance(obj, ConstructionObject):
        if obj in subs:
            return subs[obj]
        comps = tuple(normalize(comp, keys, names, subs) for comp in obj.components)
        new_obj = obj.constructor(*comps)
        names.add(new_obj.name)
        subs[obj] = new_obj
        keys[get_eqn_key(new_obj)] = get_eqn_key(obj)

        # Angles and orientations are weird, since they are anti-symmetric,
        # and can be flipped non-trivially by symmmetries of triangles.
        # Thus, when handling angles, we also have to add their reverse.
        if obj.constructor.name in ('angle', 'orientation'):
            a, b, c = obj.components
            rev = obj.constructor(c, b, a)
            normalize(rev, keys, names, subs)

        # The required predicates are also going to appear in the pattern. We need to make sure they are normalized as well.
        for req in obj.requirements():
            normalize(req, keys, names, subs)

        return new_obj
    elif isinstance(obj, GeoObject):
        if obj in subs:
            return subs[obj]
        if obj.type == LITERAL:
            return obj
        i = 0
        while f'{TYPE_NAMES[obj.type]}{i}' in names:
            i += 1
        new_name = f'{TYPE_NAMES[obj.type]}{i}'
        new_obj = Atom(new_name, obj.type)
        keys[get_eqn_key(new_obj)] = get_eqn_key(obj)
        subs[obj] = new_obj
        names.add(new_name)
        return new_obj  # type: ignore

    elif isinstance(obj, Predicate):
        res = predicate_from_args(obj.name, tuple(normalize(comp, keys, names, subs) for comp in obj.components))
        preds = unpack_predicate_full(obj)
        for sub_pred in preds:
            if sub_pred != obj:
                normalize(sub_pred, keys, names, subs)
            if sub_pred.name == 'equals' and sub_pred.components[0].type in (LITERAL, SCALAR, ANGLE):
                factors = get_linear_eqn_factors(sub_pred)
                if factors is None:
                    factors = get_log_eqn_factors(sub_pred)
                assert factors is not None
                for comp in factors:
                    normalize(comp, keys, names, subs)

        return res
    else:
        raise GeometryError(f'Attempted to normalize unknown object: {obj}!')


class Pattern(abc.ABC):
    """
    A class representing a pattern that should be matched.
    """

    old_matches: RustMatch
    """The previously known matches to the pattern."""
    new_matches: RustMatch
    """New matches to the pattern."""
    all_matches: RustMatch
    """All the matches to the pattern. This should always be equal to `RustMatch.concat([old_matches, new_matches])`"""
    name: str
    """The name of the pattern."""

    def __init__(self):
        self.old_matches = RustMatch.zero()
        self.new_matches = RustMatch.zero()
        self.all_matches = RustMatch.zero()
        self.name = ''

    def __len__(self) -> int:
        """
        The number of matches to the pattern.
        """
        return len(self.all_matches)

    def has_unpushed_data(self) -> bool:
        """
        Whether the pattern has new matches that were not propagated to all its consumers.
        """
        return len(self.new_matches) > 0

    def mark_pushed(self):
        """
        Marks that all the new matches of the pattern were propagated.
        """
        assert len(self.old_matches) + len(self.new_matches) == len(
            self.all_matches
        ), f'For pattern {self}, {len(self.old_matches)=} + {len(self.new_matches)=} != {len(self.all_matches)=}'

        self.old_matches = self.all_matches.clone()
        self.new_matches = RustMatch.zero()

    @abc.abstractmethod
    def full_repr(self, depth=0) -> str: ...

    def __repr__(self) -> str:
        return self.name


class InternalNodePattern(Pattern):
    @abc.abstractmethod
    def update(self):
        """
        Pulls all the updates from the patterns this pattern is dependent on.
        """
        ...


class IntersectPattern(InternalNodePattern):
    """
    A pattern whose matches are all substitutions that match some pattern subset.
    """

    components: 'list[Pattern]'
    """The patterns whose intersection is the given pattern."""
    accumulators: list[RustMatch]
    """A list of partial intersections of the component patterns. `accumulators[i]` is the intersection of the `all_matches` of `components[:i+1]."""

    last_reorder: int

    def __init__(self, components: Sequence[Pattern], name: str):
        """
        Initializes the intersection pattern from the sequence of sub-patterns whose intersection is the given pattern.

        Parameters:
        * `components`: A sequence of patterns.
        * `name`: The name of the intersection pattern, used to make debugging easier.
        """
        super().__init__()
        self.name = name
        self.components = list(components)
        self.accumulators = [RustMatch.zero() for _ in self.components]
        self.last_reorder = 0

    @staticmethod
    def pattern_keys(pattern: Pattern) -> set[GeoObject]:
        """
        Returns the raw objects referenced by the pattern.
        """
        return {
            KNOWN_KEYS[k]
            for k in pattern.all_matches.keys()
            if not isinstance(KNOWN_KEYS[k], EquationObject)
            and not isinstance(KNOWN_KEYS[k], ConstructionObject)
            and isinstance(KNOWN_KEYS[k], GeoObject)
        }

    def reorder(self):
        """
        Attempts to reorder the components and accumulators, so that the overall number of options checked is minimal.
        """
        if max(len(acc) for acc in self.accumulators) < 2 * self.last_reorder:
            return

        # Gathering the components.
        full_data: list[tuple[Pattern, int, set[GeoObject]]] = [
            (comp, len(comp.all_matches) + 2, IntersectPattern.pattern_keys(comp)) for comp in self.components
        ]

        curr_keys = set()
        new_order = []
        while full_data:
            next_comp = min(full_data, key=lambda t: t[1] ** (len(t[2] - curr_keys) / max(len(t[2]), 1)))
            new_order.append(next_comp[0])
            full_data.remove(next_comp)
            curr_keys |= next_comp[2]

        self.components = new_order
        # Recalculating the accumulators.
        acc = RustMatch.one()
        self.accumulators = [(acc := acc.product(comp.old_matches)) for comp in self.components]
        self.last_reorder = max(len(acc) for acc in self.accumulators)

    def print_full(self):
        """
        Prints data regarding the intersection pattern and why it is buggy.
        """
        print('IntersectPattern::print_full')
        print(self.full_repr())
        new_matches = RustMatch.zero()
        for i in range(len(self.components)):
            print(
                f'Adding {self.components[i]} (all={len(self.components[i])}) keys=({IntersectPattern.pattern_keys(self.components[i])})'
            )
            if i == 0:
                new_matches = self.components[0].new_matches.clone()
            else:
                new_matches = RustMatch.concat(
                    [
                        new_matches.product(self.components[i].all_matches),
                        self.accumulators[i - 1].product(self.components[i].new_matches),
                    ]
                )
            print(f'New matches: {len(new_matches)}')
            print(f'Acc: {len(self.accumulators[i])}')

    def update(self):
        """
        Accumulates the new additions to the sub-patterns into the current pattern.
        """
        # print(f'IntersectPattern: {self.repr()}')

        if not any(comp.has_unpushed_data() for comp in self.components):
            return
        self.reorder()
        new_matches = RustMatch.zero()
        has_printed = True
        for i in range(len(self.components)):
            if i == 0:
                new_matches = self.components[0].new_matches.clone()
            else:
                new_matches = RustMatch.concat(
                    [
                        new_matches.product(self.components[i].all_matches),
                        self.accumulators[i - 1].product(self.components[i].new_matches),
                    ]
                )
            # print(f'IntersectionPattern::update: {self.accumulators[i].keys()} {len(self.accumulators[i])} {self.accumulators[i].is_illegal()}')
            if len(new_matches) > 0:
                self.accumulators[i] = RustMatch.concat([self.accumulators[i], new_matches])
                # print('=====')
                # print(len(new_matches))
                # print(self.repr())
            if len(self.accumulators[i]) > 100000 and not has_printed:
                self.print_full()
                has_printed = True

        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

        if len(self.all_matches) > MAX_INTERSECTION_PATTERN_MATCHES:
            warnings.warn(f'Pattern {self.full_repr()} reached overload!')

    def full_repr(self, idx=0) -> str:
        name = self.name if self.name else 'Intersect'
        return (
            '\t' * idx
            + f'{name} ({len(self.all_matches)}):\n'
            + '\n'.join(comp.full_repr(idx + 1) for comp in self.components)
        )


class RawObjPattern(Pattern):
    """
    A pattern representing the matches to a given construction object.
    The object pattern contains only a single, non-recursive, construction.
    Recursive constructions (Such as center(Circle(a, b, c))) have to be constructed by the intersection of two patterns.
    """

    object: GeoObject

    def __init__(self, theorem_obj: GeoObject):
        """
        Initializes the ObjPattern.
        """
        super().__init__()
        self.object = theorem_obj
        self.name = f'RawObjPattern({theorem_obj.name})'
        assert not isinstance(self.object, EquationObject)

    def add_object(self, representative: GeoObject, obj: GeoObject):
        """
        Adds an object to the raw object pattern.

        Parameters:
        * `representative`: The representative object.
        * `obj`: The represented object, that might give new constructions for the representative.
        """
        if isinstance(obj, EquationObject):
            return
        if obj.type != self.object.type:
            return
        if isinstance(self.object, ConstructionObject):
            if not isinstance(obj, ConstructionObject):
                return
            if self.object.constructor != obj.constructor:
                return
            # At this point, the keys might not be unique, and the values might not agree with the keys.
            base_keys = [get_eqn_key(comp) for comp in self.object.components]
            base_values = tuple(get_eqn_key(comp) for comp in obj.components)
            base_values = [list(order) for order in self.object.constructor.symmetry.all_orders(base_values)]  # type: ignore

            keys = list(set(base_keys)) + [get_eqn_key(self.object)]
            values = []
            for order in base_values:
                d = {get_eqn_key(self.object): get_eqn_key(representative)}
                good = True
                for k, v in zip(base_keys, order):
                    if k not in d:
                        d[k] = v
                    elif d[k] != v:
                        good = False
                if not good:
                    continue
                values.append([d[k] for k in keys])

            new_matches = RustMatch.raw(keys, values)
        else:
            new_matches = RustMatch.of(get_eqn_key(self.object), get_eqn_key(obj))

        new_matches = new_matches.subtract(self.all_matches)
        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

    def full_repr(self, idx=0) -> str:
        return '\t' * idx + f'RawObj({self.object}: {get_eqn_key(self.object)}) ({len(self.all_matches)})'


class RawPredicatePattern(Pattern):
    """
    A pattern representing the raw matches to a predicate, without caring about the constructions.
    """

    pred: Predicate

    def __init__(self, theorem_pred: Predicate):
        super().__init__()
        self.pred = theorem_pred
        assert self.pred.name != 'equals_mod_360'
        if self.pred.name == 'equals':
            assert self.pred.components[0].type in (POINT, LINE, CIRCLE)
        self.name = f'RawPredPattern{theorem_pred.name}'

    def add_predicate(self, pred: Predicate):
        """
        Adds a predicate to the pattern.
        """
        if pred.name != self.pred.name:
            return
        if len(pred.components) != len(self.pred.components):
            return

        # At this point, the keys might not be unique, and the values might not agree with the keys.
        base_keys = [get_eqn_key(comp) for comp in self.pred.components]
        base_values = tuple(get_eqn_key(comp) for comp in pred.components)
        base_values = [list(order) for order in pred.symmetry.all_orders(base_values)]  # type: ignore

        keys = list(set(base_keys))
        values = []
        for order in base_values:
            d = {}
            good = True
            for k, v in zip(base_keys, order):
                if k not in d:
                    d[k] = v
                elif d[k] != v:
                    good = False
            if not good:
                continue
            values.append([d[k] for k in keys])

        new_matches = RustMatch.raw(keys, values)

        new_matches = new_matches.subtract(self.all_matches)
        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

    def full_repr(self, idx=0) -> str:
        return '\t' * idx + f'RawPred({self.pred}) ({len(self.all_matches)})'


class EquationPattern(InternalNodePattern):
    """
    A pattern representing an equation, such as X + Y - Z.
    """

    geometry_tracker: GeometryTracker
    coef_keys: list[int]
    eqn_factors: list[int]
    const_factor: int
    mod: int | None
    types: list[str]

    def __init__(
        self,
        geometry_tracker: GeometryTracker,
        coef_keys: list[int],
        eqn_factors: list[int],
        const_factor: int,
        mod: int | None,
        types: list[str],
    ):
        """
        Initializes the equation pattern.
        """
        assert isinstance(coef_keys, list)
        super().__init__()
        self.geometry_tracker = geometry_tracker
        self.coef_keys = coef_keys
        self.eqn_factors = eqn_factors
        self.const_factor = const_factor
        self.mod = mod
        self.types = types
        self.name = f'EqPattern({coef_keys=}, {const_factor=}, {mod=}, {types=})'

    def update(self):
        """
        Updates the equation pattern using the proof checker.
        """
        match self.mod:
            case 2:
                tracker = self.geometry_tracker._linear_algebra._bool_equations
            case 360:
                tracker = self.geometry_tracker._linear_algebra._mod_360_equations
            case None:
                tracker = self.geometry_tracker._linear_algebra._real_equations
            case _:
                raise NotImplementedError(f'Equations mod {self.mod} are not implemented!')

        r_inputs = [
            [obj for obj in self.geometry_tracker.unique_objects() if extended_type(obj) == typ] for typ in self.types
        ]

        combinations = tracker.find_combinations(self.eqn_factors, self.const_factor, r_inputs)
        combination_indices = [[get_eqn_key(o) for o in lst] for lst in combinations]

        new_matches = RustMatch.raw(self.coef_keys, combination_indices).subtract(self.all_matches)
        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

    def full_repr(self, idx=0) -> str:
        return (
            '\t' * idx
            + f'Eq({self.types}, keys={self.coef_keys} factors={self.eqn_factors}, const={self.const_factor}) (len={len(self)})'
        )


class NonzeroPattern(InternalNodePattern):
    """
    A pattern representing a not-equals condition, such as X + Y - Z != 0.
    """

    geometry_tracker: GeometryTracker
    eqn_factors: list[int]
    const_factor: int
    mod: int | None
    types: list[
        str
    ]  # The types are either the raw types, for GeoObjects, or the constructor names. This should capture everything.
    found_nonzeros: set[tuple[GeoObject, ...]]

    def __init__(
        self,
        geometry_tracker: GeometryTracker,
        coef_keys: list[int],
        eqn_factors: list[int],
        const_factor: int,
        mod: int | None,
        types: list[str],
    ):
        """
        Initializes the equation pattern.

        Parameters:
        * `checker`: The ProofChecker containing the linear algebra trackers.
        * `coef_keys`: The equation keys of the objects in the nonzero. In the example above, this would be (get_eqn_key(X), get_eqn_key(Y), get_eqn_key(Z)).
        * `const_factor`: If there is a constant factor in the equation. In `X - 90 != 0`, this would be `-90`.
        * `mod`: The modulus of the equation.
        * `type`: The type of the objects in the equation, such as Angle or Scalar.
        """
        assert isinstance(coef_keys, list)
        super().__init__()
        self.geometry_tracker = geometry_tracker
        self.coef_keys = coef_keys
        self.eqn_factors = eqn_factors
        self.const_factor = const_factor
        self.mod = mod
        self.types = types
        self.name = f'NonzeroPattern({coef_keys=}, {const_factor=}, {mod=}, {types=})'
        self.found_nonzeros = set()

    def update(self):
        """
        Updates the equation pattern using the proof geometry tracker.
        """
        match self.mod:
            case 2:
                tracker = self.geometry_tracker._linear_algebra._bool_equations
            case 360:
                tracker = self.geometry_tracker._linear_algebra._mod_360_equations
            case None:
                tracker = self.geometry_tracker._linear_algebra._real_equations
            case _:
                raise NotImplementedError(f'Equations mod {self.mod} are not implemented!')

        objects = [[u for u in self.geometry_tracker.unique_objects() if extended_type(u) == typ] for typ in self.types]

        res: list[list[int]] = []
        for curr_objs in itertools.product(*objects):
            key = tuple(curr_objs)
            if key in self.found_nonzeros:
                continue

            comb = {}
            for obj, val in zip(curr_objs, self.eqn_factors):
                comb[obj] = comb.get(obj, 0) + val

            if tracker.contains_nonzero(comb):
                curr_objs = [get_eqn_key(obj) if obj is not None else get_eqn_key(ONE) for obj in curr_objs]
                res.append(curr_objs)
                self.found_nonzeros.add(key)

        new_matches = RustMatch.raw(self.coef_keys, res).subtract(self.all_matches)
        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

    def full_repr(self, idx=0) -> str:
        return (
            '\t' * idx
            + f'Eq({self.types}, keys={self.coef_keys} factors={self.eqn_factors}, const={self.const_factor}) (len={len(self)})'
        )


class RekeyPattern(InternalNodePattern):
    """
    A pattern that is equal to another pattern with different keys.
    """

    data: Pattern
    keys: dict[int, int]

    def __init__(self, pat: Pattern, keys: dict[int, int]):
        super().__init__()
        self.data = pat
        self.keys = keys
        self.keys[get_eqn_key(ONE)] = get_eqn_key(ONE)
        self.name = f'Rekey({self.data.name})'

    def update(self):
        if not all(old_key in self.keys for old_key in self.data.all_matches.keys()):
            print('Exception in:')
            print(self.full_repr())
            print(f'Old keys: {[KNOWN_KEYS[key] for key in self.data.all_matches.keys()]}')
            print(f'Self keys: { {KNOWN_KEYS[key]: KNOWN_KEYS[val] for key, val in self.keys.items()} }')
            print('Missing keys:')
            for old_key in self.data.all_matches.keys():
                if old_key not in self.keys:
                    print(f'Key: {old_key}: {KNOWN_KEYS[old_key]} {type(KNOWN_KEYS[old_key])}')

        new_matches = self.data.new_matches.map_keys(self.keys)
        self.new_matches.extend(new_matches)
        self.all_matches.extend(new_matches)

    def full_repr(self, depth=0) -> str:
        return '\t' * depth + f'Rekeyed: ({self.mapping()})\n' + self.data.full_repr(depth)

    def mapping(self) -> dict[GeoObject, GeoObject]:
        """
        Returns the dictionary mapping keys in the old pattern to new keys.
        """
        return {KNOWN_KEYS[k]: KNOWN_KEYS[v] for k, v in self.keys.items()}


class SignatureDag:
    """
    A class for quickly finding all possible steps matching some list of patterns.

    Big TODO list:
    * Add a pattern to the conclusion of the proof generation, for when one needs to construct objects and not only to prove predicates.
      This would also require a constant pattern, matching only a single object.
    * Make the EqualPattern store its own sub-patterns, and find only combinations using at least one new object.
    """

    sorted_patterns: list[Pattern]
    """The patterns in the DAG, sorted by some topological sorting."""
    raw_object_patterns: dict[GeoObject, RawObjPattern]
    """The GeoObject patterns in the DAG."""
    object_patterns: dict[GeoObject, Pattern]
    """The patterns of all GeoObjects."""
    raw_predicate_patterns: dict[Predicate, RawPredicatePattern]
    """The raw predicates in the DAG."""
    raw_nonzero_patterns: dict[tuple[tuple[int, ...], int, int | None, tuple[str, ...]], NonzeroPattern]
    """The raw patterns of nonzero combinations."""
    raw_equation_patterns: dict[tuple[tuple[int, ...], int, int | None, tuple[str, ...]], EquationPattern]
    """The raw patterns of combinations that are zero."""

    predicate_patterns: dict[Predicate, Pattern]
    """The predicates in the DAG."""
    step_patterns: dict[Pattern, Theorem | Construction]
    """The end-patterns for theorems."""

    step_key_to_obj: dict[int, GeoObject]
    """A map from the keys of objects in the patterns to the real objects."""

    processed_objects: UnionFind[GeoObject]
    """All objects that were added to the patterns."""
    processed_predicates: set[Predicate]
    """All predicates that were added to the patterns."""

    _new_steps: list[tuple[Theorem | Construction, frozendict[GeoObject, GeoObject]]]
    """The queue of the next steps to take."""
    geometry_tracker: GeometryTracker
    """The proof checker in which we search for patterns."""

    def __init__(self, geometry_tracker: GeometryTracker, steps: Sequence[Theorem | Construction]):
        self.sorted_patterns = []
        self.step_patterns = {}
        self.raw_object_patterns = {}
        self.raw_predicate_patterns = {}
        self.raw_nonzero_patterns = {}
        self.raw_equation_patterns = {}
        self.object_patterns = {}
        self.predicate_patterns = {}
        self.processed_objects = UnionFind()
        self.processed_predicates = set()
        self.step_queue = []
        self._new_steps = []
        self.geometry_tracker = geometry_tracker
        self.step_key_to_obj = {get_eqn_key(ONE): ONE, get_eqn_key(ZERO): ZERO}

        # Adding all the theorems.
        for step in steps:
            if isinstance(step, Theorem):
                self.make_theorem_pattern(step)
            elif isinstance(step, Construction):
                self.make_construction_pattern(step)
            else:
                raise TypeError(f'SignatureDag received unknown step: {step}!')

    def get_rekey_pattern(self, pattern: Pattern, keys: dict[int, int]) -> RekeyPattern:
        res = RekeyPattern(pattern, keys)
        self.sorted_patterns.append(res)
        return res

    def get_raw_object_pattern(self, obj: GeoObject) -> RawObjPattern:
        """
        Gets the pattern storing matches to the given object, treated as a non-recursive construction.
        """
        if obj in self.raw_object_patterns:
            return self.raw_object_patterns[obj]

        res = RawObjPattern(obj)
        self.raw_object_patterns[obj] = res
        self.sorted_patterns.append(res)

        return res

    def get_object_pattern(self, obj: GeoObject) -> Pattern:
        """
        Gets the pattern storing matches to the given objects, treated as a recursive constrution.

        Parameters:
        * `obj`: An object appearing in a theorem.

        Return:

        A pattern matching all objects in the proof checker the theorem object can be substituted to.
        """
        # Attempting to normalize the object.
        keys = {}
        norm_obj = normalize(obj, keys)
        if norm_obj != obj:
            return self.get_rekey_pattern(self.get_object_pattern(norm_obj), keys)

        if obj in self.object_patterns:
            return self.object_patterns[obj]

        assert not isinstance(obj, EquationObject)
        if isinstance(obj, ConstructionObject):
            patterns = []
            for comp in involved_objects(obj):
                patterns.append(self.get_raw_object_pattern(comp))
            if len(patterns) == 1:
                return patterns[0]
            res = IntersectPattern(patterns, name=obj.to_language_format())
        else:
            res = self.get_raw_object_pattern(obj)

        self.object_patterns[obj] = res
        self.sorted_patterns.append(res)
        return res

    def get_raw_predicate_pattern(self, pred: Predicate) -> RawPredicatePattern:
        if pred in self.raw_predicate_patterns:
            return self.raw_predicate_patterns[pred]

        raw_pred = RawPredicatePattern(pred)
        self.sorted_patterns.append(raw_pred)
        self.raw_predicate_patterns[pred] = raw_pred
        return raw_pred

    def get_raw_nonzero_pattern(self, pred: Predicate) -> Pattern:
        """
        Gets a pattern matching a nonzero predicate.
        """
        eqn_factors = get_linear_eqn_factors(pred)
        if eqn_factors is None:
            eqn_factors = get_log_eqn_factors(pred)
        if eqn_factors is None:
            raise GeometryError(f'Predicate could not be converted to an equation: {pred}!')

        type_ = pred.components[0].type if pred.components[0].type != LITERAL else pred.components[1].type

        if pred.name == 'not_equals' and type_ in (ANGLE, SCALAR, LITERAL):
            mod = None
        elif pred.name == 'not_equals' and type_ == ORIENTATION:
            mod = 2
        elif pred.name == 'not_equals_mod_360':
            mod = 360
        else:
            raise GeometryError(f'Illegal predicate: {pred}')

        const_factor = 0
        if ONE in eqn_factors:
            const_factor = eqn_factors.pop(ONE)
        assert abs(const_factor - round(const_factor)) < 1e-3
        const_factor = int(round(const_factor))

        coef_keys = []
        coef_values = []
        for obj, val in eqn_factors.items():
            coef_keys.append(obj)
            coef_values.append(val)

        types = [extended_type(obj) for obj in coef_keys]
        coef_keys = [get_eqn_key(obj) for obj in coef_keys]

        key = (tuple(coef_values), const_factor, mod, tuple(types))

        if key in self.raw_nonzero_patterns:
            old_pat = self.raw_nonzero_patterns[key]
            res = RekeyPattern(old_pat, {old_key: curr_key for old_key, curr_key in zip(old_pat.coef_keys, coef_keys)})
            self.sorted_patterns.append(res)
            return res

        res = NonzeroPattern(self.geometry_tracker, coef_keys, coef_values, const_factor, mod, types)
        self.sorted_patterns.append(res)
        self.raw_nonzero_patterns[key] = res
        return res

    def get_raw_equation_pattern(self, pred: Predicate) -> Pattern:
        """
        Gets a pattern matching a nonzero predicate.
        """
        eqn_factors = get_linear_eqn_factors(pred)
        if eqn_factors is None:
            eqn_factors = get_log_eqn_factors(pred)
        if eqn_factors is None:
            raise GeometryError(f'Predicate could not be converted to an equation: {pred}!')

        type_ = pred.components[0].type if pred.components[0].type != LITERAL else pred.components[1].type

        if pred.name == 'equals' and type_ in (ANGLE, SCALAR, LITERAL):
            mod = None
        elif pred.name == 'equals' and type_ == ORIENTATION:
            mod = 2
        elif pred.name == 'equals_mod_360':
            mod = 360
        else:
            raise GeometryError(f'Illegal predicate: {pred}')

        # Step 1. Gathering the data.
        const_factor = 0
        if ONE in eqn_factors:
            const_factor = eqn_factors.pop(ONE)
        assert abs(const_factor - round(const_factor)) < 1e-3
        const_factor = int(round(const_factor))
        coef_keys = []
        coef_values = []
        for obj, val in eqn_factors.items():
            coef_keys.append(obj)
            coef_values.append(val)
        types = [extended_type(obj) for obj in coef_keys]
        coef_keys = [get_eqn_key(obj) for obj in coef_keys]

        # Step 2. Sorting the keys, values, and types.
        ord = sorted(range(len(coef_values)), key=lambda i: coef_values[i])
        types = [types[ord[i]] for i in range(len(types))]
        coef_keys = [coef_keys[ord[i]] for i in range(len(coef_keys))]
        coef_values = [coef_values[ord[i]] for i in range(len(coef_keys))]
        key = (tuple(coef_values), const_factor, mod, tuple(types))

        if key in self.raw_equation_patterns:
            old_pat = self.raw_equation_patterns[key]
            res = RekeyPattern(old_pat, {old_key: curr_key for old_key, curr_key in zip(old_pat.coef_keys, coef_keys)})
            self.sorted_patterns.append(res)
            return res

        res = EquationPattern(self.geometry_tracker, coef_keys, coef_values, const_factor, mod, types)
        self.sorted_patterns.append(res)
        self.raw_equation_patterns[key] = res
        return res

    def get_predicate_pattern(self, pred: Predicate) -> Pattern:
        """
        Gets the pattern for matches of a given predicate.
        """
        # Checking if the predicate was already found.
        if pred in self.predicate_patterns:
            return self.predicate_patterns[pred]

        # Checking if the normalized predicate were already found.
        keys = {}
        norm_pred = normalize(pred, keys)
        if norm_pred != pred:
            # print(f'get_predicate_pattern: {norm_pred} => {pred}')
            # print({KNOWN_KEYS[key]: KNOWN_KEYS[val] for key, val in keys.items()})
            res = self.get_rekey_pattern(self.get_predicate_pattern(norm_pred), keys)

            # if pred.name == 'inside_infinite_hourglass' and isinstance(pred.components[0], ConstructionObject):
            #     print('SignatureDag::get_predicate_pattern')
            #     print(res.repr())
            #     print(res.mapping())

            self.predicate_patterns[pred] = res
            self.sorted_patterns.append(res)
            return res

        unpack = unpack_predicate_minimal(pred)
        if len(unpack) > 1:
            pred_patterns = [self.get_predicate_pattern(sub_pred) for sub_pred in unpack]
            res = IntersectPattern(pred_patterns, pred.to_language_format())
            self.sorted_patterns.append(res)
            self.predicate_patterns[pred] = res
            return res

        # Trying to use equation patterns connected to the linear algebra trackers.
        if pred.name in ('equals', 'equals_mod_360') and (
            pred.components[0].type in EQN_TYPES or pred.components[1] in EQN_TYPES
        ):
            eqn_factors = get_linear_eqn_factors(pred)
            if eqn_factors is None:
                eqn_factors = get_log_eqn_factors(pred)
            if eqn_factors is None:
                raise GeometryError(f'Predicate could not be converted to an equation: {pred}!')

            coef_keys = []
            coef_values = []
            for obj, val in eqn_factors.items():
                coef_keys.append(obj)
                coef_values.append(val)

            obj_pats: list[Pattern] = [self.get_object_pattern(obj) for obj in coef_keys]
            coef_keys = [get_eqn_key(obj) for obj in coef_keys]

            eq_pat = self.get_raw_equation_pattern(pred)
            pred_pattern = IntersectPattern([eq_pat] + obj_pats, pred.to_language_format())
            self.predicate_patterns[pred] = pred_pattern
            self.sorted_patterns.append(pred_pattern)
            return pred_pattern

        elif pred.name in ('not_equals', 'not_equals_mod_360') and (
            pred.components[0].type in EQN_TYPES or pred.components[1] in EQN_TYPES
        ):
            eqn_factors = get_linear_eqn_factors(pred)
            if eqn_factors is None:
                eqn_factors = get_log_eqn_factors(pred)
            if eqn_factors is None:
                raise GeometryError(f'Predicate could not be converted to an equation: {pred}!')

            coef_keys = []
            coef_values = []
            for obj, val in eqn_factors.items():
                coef_keys.append(obj)
                coef_values.append(val)

            obj_pats: list[Pattern] = [self.get_object_pattern(obj) for obj in coef_keys]
            coef_keys = [get_eqn_key(obj) for obj in coef_keys]

            eq_pat = self.get_raw_nonzero_pattern(pred)
            pred_pattern = IntersectPattern([eq_pat] + obj_pats, pred.to_language_format())
            self.predicate_patterns[pred] = pred_pattern
            self.sorted_patterns.append(pred_pattern)
            return pred_pattern
        else:
            # If the pattern is not an equation, we use the raw predicate pattern.
            pred_pattern = self.get_raw_predicate_pattern(pred)
            # We also need to match the construction patterns.
            object_patterns: list[Pattern] = [self.get_object_pattern(obj) for obj in involved_objects(pred)]

            res = IntersectPattern(object_patterns + [pred_pattern], pred.to_language_format())
            self.sorted_patterns.append(res)
            self.predicate_patterns[pred] = res
            return res

    def make_theorem_pattern(self, theorem: Theorem):
        for obj in involved_objects(theorem):
            self.step_key_to_obj[get_eqn_key(obj)] = obj
        patterns = []
        for comp in involved_objects(theorem):
            patterns.append(self.get_object_pattern(comp))
        for pred in theorem.required_predicates:
            # Large open predicates, such as distinct(A, B, C, D, E), tend to take up a lot of resources.
            # By unpacking them, we can intersect them with closed predicates and avoid the blow-up.
            if pred.is_open() or pred.name in {'in', 'exists'}:
                patterns.extend(self.get_predicate_pattern(sub_pred) for sub_pred in unpack_predicate_minimal(pred))
            else:
                patterns.append(self.get_predicate_pattern(pred))

        theorem_pattern = IntersectPattern(patterns, f'Theorem({theorem.name})')
        self.sorted_patterns.append(theorem_pattern)
        self.step_patterns[theorem_pattern] = theorem

    def make_construction_pattern(self, construction: Construction):
        for obj in involved_objects(construction):
            self.step_key_to_obj[get_eqn_key(obj)] = obj

        patterns = []
        for comp in involved_objects(construction):
            patterns.append(self.get_object_pattern(comp))
        for pred in construction.required_predicates:
            # Large open predicates, such as distinct(A, B, C, D, E), tend to take up a lot of resources.
            # By unpacking them, we can intersect them with closed predicates and avoid the blow-up.
            if pred.is_open() or pred.name in {'in', 'exists'}:
                patterns.extend(self.get_predicate_pattern(sub_pred) for sub_pred in unpack_predicate_minimal(pred))
            else:
                patterns.append(self.get_predicate_pattern(pred))

        construction_pattern = IntersectPattern(patterns, f'Construction({construction})')
        self.sorted_patterns.append(construction_pattern)
        self.step_patterns[construction_pattern] = construction

    def update(self):
        """
        Finds new theroems and predicates suggested by the checker.
        """
        geometry_key_to_obj = {get_eqn_key(obj): obj for obj in self.geometry_tracker.all_objects()}

        for special_obj in [ZERO, ONE]:
            geometry_key_to_obj[get_eqn_key(special_obj)] = special_obj

        # Step 1. Pushing updates to the low-level patterns.
        new_objects = [
            obj
            for obj in self.geometry_tracker.all_objects()
            if obj not in self.processed_objects
            or self.processed_objects[obj] != self.checker.get_object(obj, TRUST_NO_ADD_CFG)
        ]
        new_predicates = [pred for pred in self.geometry_tracker.all_predicates() - self.processed_predicates] + [
            predicate_from_args('equals', (obj, obj)) for obj in new_objects
        ]
        self.processed_predicates.update(new_predicates)

        # Step 1.1. Adding new predicates to the predicate patterns.
        for new_pred in new_predicates:
            for unpacked in unpack_predicate_full(new_pred):
                for pred_pattern in self.raw_predicate_patterns.values():
                    pred_pattern.add_predicate(unpacked)

        # Step 1.2. Adding new objects to the object patterns.
        for new_obj in new_objects:
            if isinstance(new_obj, ConstructionObject) and any(
                comp != self.geometry_tracker.get_object(comp, TRUST_NO_ADD_CFG) for comp in new_obj.components
            ):
                # If one of the components is not substituted, there is no point in adding the representation.
                # Note that this object should always exists, as described in the equality system specification.
                continue

            new_repr = self.geometry_tracker.get_object(new_obj, TRUST_NO_ADD_CFG)
            for obj_pattern in self.raw_object_patterns.values():
                obj_pattern.add_object(new_repr, new_obj)
        # Step 2. Pushing all the data.
        for pattern in self.sorted_patterns:
            if isinstance(pattern, InternalNodePattern):
                pattern.update()

        # Step 3. For theorem patterns, we get the new theorem steps.
        for pattern, step in self.step_patterns.items():
            for match_ in pattern.new_matches.to_dict(self.step_key_to_obj, geometry_key_to_obj):
                self._new_steps.append((step, frozendict(match_)))

        # Step 4. Marking all the data as pushed.
        for pattern in self.sorted_patterns:
            pattern.mark_pushed()

    def new_steps(self) -> list[tuple[Theorem | Construction, frozendict[GeoObject, GeoObject]]]:
        """
        Gets the new steps of the SignatureDag and clears the SignatureDag.
        """
        res = self._new_steps
        self._new_steps = []
        return res
