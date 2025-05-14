from typing import TYPE_CHECKING, Mapping
from mpmath import mp

from ..predicates.global_predicates import get_constructions
from ..symmetry import Symmetry
from ..rule_utils import LITERAL, SCALAR, ANGLE, ProofCheckError, union, GeometryError

from .atom import Atom
from .geo_object import GeoObject
from .literal import ONE, ZERO
from .equation_object import EquationObject

if TYPE_CHECKING:
    from ..predicates.predicate import Predicate

from dataclasses import dataclass, field


INPUT_LABEL = 'inputs'
PREPROCESS_LABEL = 'preprocess'
CONDITION_LABEL = 'where'
CONSTRUCTION_LABEL = 'construct'
RESULT_PREDICATE_LABEL = 'conclude'
POSS_CONCLUSIONS_LABEL = 'possible_conclusions'


@dataclass(frozen=True)
class Construction:
    """
    An object representing common ways to build objects from other objects.
    """

    name: str
    """The name of the consturction."""
    signature: 'list[GeoObject]' = field(compare=False, repr=False)
    """The types of the objects received by the construction."""
    symmetry: Symmetry
    """A preprocessing applied on the arguments of the construction."""
    res: 'GeoObject' = field(compare=False, repr=False)
    """The type of the object built by the construction."""
    required_predicates: 'list[Predicate]' = field(compare=False, repr=False, default_factory=list)
    """A list of requirements on the objects used to construct the ConstructionObject."""
    result_predicates: 'list[Predicate]' = field(compare=False, repr=False, default_factory=list)
    """A list of predicates satisfied by the constructed object."""
    possible_conclusions: 'list[tuple[list[Predicate], list[Predicate]]]' = field(
        compare=False, repr=False, default_factory=list
    )

    def canonical_name(self, *args: 'GeoObject'):
        """
        Returns the canonical name of the construction object built using the given arguments.
        """
        return f'{self.name}({", ".join(obj.name for obj in args)})'

    def __call__(self, *args: 'GeoObject') -> 'ConstructionObject':
        """
        Constructs an object using the given arguments.
        """
        if len(args) != len(self.signature) or not all(
            arg.type == sig.type or (arg.type == LITERAL and sig.type in [SCALAR, ANGLE])
            for arg, sig in zip(args, self.signature)
        ):
            raise ProofCheckError(f'Construction {self.name} received illegal arguments: {args}')

        args = self.symmetry.canonical_order(args)
        name = self.canonical_name(*args)
        return ConstructionObject(name, self.res.type, self, args)

    def __repr__(self) -> str:
        return f'Construction({self.name})'


class ConstructionObject(Atom):
    """
    A geometric object constructed from several sub-objects.
    """

    __slots__ = 'constructor', 'components'
    constructor: Construction
    components: tuple[GeoObject, ...]

    def __init__(
        self, name: str, type: str, constructor: Construction, components: tuple[GeoObject, ...], id: int | None = None
    ):
        self.name = name
        self.type = type
        self.constructor = constructor
        self.components = components
        self.id = id or hash(self.name)
        self.depth = max([component.depth for component in components]) + 1

    def substitute(self, replacements: Mapping[GeoObject, GeoObject], ignore_self=False) -> GeoObject:
        if self in replacements and not ignore_self:
            return replacements[self]
        return self.constructor(*(comp.substitute(replacements) for comp in self.components))

    @staticmethod
    def from_args(const_name: str, args: tuple[GeoObject, ...]) -> 'GeoObject':
        const = get_constructions().get(const_name, None)

        if const is None:
            print(get_constructions())
            raise GeometryError(f'Illegal construction used: {const_name}!')
        res = const(*args)
        return res

    def __repr__(self) -> str:
        return self.name

    def requirements(self) -> 'list[Predicate]':
        """
        Returns the list of predicates required by the construction object.
        """
        subs = {sig: comp for sig, comp in zip(self.constructor.signature, self.components)}
        subs[self.constructor.res] = self
        return [pred.substitute(subs) for pred in self.constructor.required_predicates]

    def conclusions(self) -> 'list[Predicate]':
        """
        Returns the list of predicates created by the construction object.
        """
        subs = {sig: comp for sig, comp in zip(self.constructor.signature, self.components)}
        subs[self.constructor.res] = self
        return [pred.substitute(subs) for pred in self.constructor.result_predicates]

    def possible_conclusions(self) -> 'list[tuple[list[Predicate], list[Predicate]]]':
        """
        Returns the list of predicates created by the construction object.
        """
        subs = {sig: comp for sig, comp in zip(self.constructor.signature, self.components)}
        subs[self.constructor.res] = self

        return [
            ([pred.substitute(subs) for pred in left], [pred.substitute(subs) for pred in right])
            for left, right in self.constructor.possible_conclusions
        ]

    def clone(self) -> 'ConstructionObject':
        return ConstructionObject(self.name, self.type, self.constructor, self.components)

    def involved_objects(self) -> set[GeoObject]:
        return super().involved_objects() | union(comp.involved_objects() for comp in self.components)


@dataclass(frozen=True)
class LogConstruction(Construction):
    """
    Constructs the log of an object.
    When taking the log of an equation, we might have log(2*X), which should be translated to log(X) + log(2),
    or an equation which is a scalar.
    """

    def __call__(self, *args) -> GeoObject:
        assert len(args) == 1, f'log_construction called with args {args}!'

        inp = args[0]
        if isinstance(inp, EquationObject):
            inp_log_factors = inp.as_log_equation()
            if inp_log_factors is not None:
                return sum((obj * factor for obj, factor in inp_log_factors.items()), ZERO)

        # The special conversion failed.
        return super().__call__(*args)


def as_log_equation(self) -> dict[GeoObject, float] | None:
    if (val := self.as_literal()) is not None:
        if val <= 0:
            return None
        return {ONE: mp.log(val)}
    if self.type == SCALAR:
        return {ConstructionObject.from_args('log', (self,)): 1}
    return None


GeoObject.as_log_equation = as_log_equation
