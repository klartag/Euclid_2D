from .geometry_objects.geo_type import GeoType
from .geometry_objects.geo_object import GeoObject
from .predicates.predicate import Predicate


KNOWN_KEYS: dict[int, GeoObject] = {}


def get_eqn_key(obj: GeoObject) -> int:
    """
    Returns the key in which the object is stored in the linear algebra trackers.
    """
    global KNOWN_KEYS
    res = hash(obj)
    if res not in KNOWN_KEYS:
        KNOWN_KEYS[res] = obj
    return hash(obj)


def get_linear_eqn_factors(pred: Predicate) -> dict[GeoObject, float] | None:
    """
    Gets the predicate as a linear equation.
    """
    assert pred.name.startswith('equals')
    res = (pred.components[0] - pred.components[1]).as_linear_equation()
    if res is None:
        return None
    assert not any(
        obj.type == GeoType.LITERAL and obj.name != '1' for obj in res
    ), f'Illegal unpack: {pred.to_language_format()} => {res}'
    return res


def get_log_eqn_factors(pred: Predicate) -> dict[GeoObject, float] | None:
    """
    Gets the predicate as a log equation.
    This is not defined for equals_mod.
    """
    assert pred.name == 'equals'
    left_log = pred.components[0].as_log_equation()
    right_log = pred.components[1].as_log_equation()
    if left_log is None or right_log is None:
        return None
    for obj, factor in right_log.items():
        left_log[obj] = left_log.get(obj, 0) - factor
    assert not any(
        obj.type == GeoType.LITERAL and obj.name != '1' for obj in left_log
    ), f'Illegal unpack: {pred.to_language_format()} => {left_log}'
    return left_log


def get_raw_eqn_factors(factors: dict[GeoObject, float]) -> dict[int, float]:
    return {get_eqn_key(key): val for key, val in factors.items()}


def unpack_predicate_full(pred: Predicate) -> set[Predicate]:
    """
    Unpacks the given predicate, to find all predicates implied by it.
    Makes sure that in the unpacked result, every predicate appears once.
    @pred: A predicate.
    @return: A set containing all predicates implied by the given predicate.
    """
    stack = [pred]
    handled = set()
    res = set()
    while stack:
        top = stack.pop()
        if top in handled:
            continue
        handled.add(top)
        unpacked_top = top.unpack()
        if top in unpacked_top:
            res.add(top)
        stack.extend(unpacked_top)

    return res


def unpack_predicate_minimal(pred: Predicate) -> set[Predicate]:
    """
    Unpacks a predicate to find a small set of predicates that are both implied
    by the predicate and sufficient for it to be satisfied.
    Works the same way as the full unpacker, but doesn't unpack a predicate if it is not a macro.
    """
    stack = [pred]
    handled = set()
    res = set()
    while stack:
        top = stack.pop()
        if top in handled:
            continue
        handled.add(top)
        unpacked_top = top.unpack()
        if top in unpacked_top:
            res.add(top)
        else:
            stack.extend(unpacked_top)

    return res
