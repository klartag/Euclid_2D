from dataclasses import dataclass
from fractions import Fraction

from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.geo_type import GeoType
from ..geometry_objects.construction_object import ConstructionObject, Construction
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.literal import ZERO


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


def as_log_equation(self) -> dict[GeoObject, Fraction] | None:
    # TODO: Document
    if (val := self.as_literal()) is not None:
        if val <= 0:
            return None
        return {ConstructionObject.from_args('log', (self,)): 1}
    if self.type == GeoType.SCALAR:
        return {ConstructionObject.from_args('log', (self,)): 1}
    return None


GeoObject.as_log_equation = as_log_equation
