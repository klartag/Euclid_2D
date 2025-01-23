from ..geometry_objects.construction_object import ConstructionObject
from ..predicates.predicate import Predicate
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject


def is_trivial(obj: Predicate | GeoObject) -> bool:
    """
    Checks if the predicate is automatically known, or is boring in some other fashion.
    """
    if isinstance(obj, Predicate):
        if any(is_trivial(comp) for comp in obj.components):
            return True
        match obj.name:
            case 'between':
                return obj.components[0] == obj.components[1] or obj.components[1] == obj.components[2]
            case 'equals':
                return obj.components[0] == obj.components[1]
            case 'concyclic':
                return len(set(obj.components)) < 4
            case _:
                return False
    elif isinstance(obj, ConstructionObject):
        if any(is_trivial(comp) for comp in obj.components):
            return True
        match obj.constructor.name:
            case 'midpoint':
                return obj.components[0] == obj.components[1]
            case 'Circle' | 'circumcircle':
                return obj.components[0] == obj.components[1] or obj.components[0] == obj.components[2] or obj.components[2] == obj.components[1]
            case 'angle':
                return obj.components[0] == obj.components[2]
            case 'distance':
                return obj.components[0] == obj.components[1]
            case 'abs' | 'abs_angle' | 'exp':
                # Why anyone would ever use `abs` is beyond me, and I have also never seen `exp` used.
                return True
            case _:
                return False
    elif isinstance(obj, EquationObject):
        return is_trivial(obj.left) or is_trivial(obj.right)
    else:
        return False
