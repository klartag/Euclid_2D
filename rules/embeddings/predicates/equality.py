from ..embedded_objects import EmbeddedObject, EmbeddedScalar, EPSILON


def equals(obj0: EmbeddedObject, obj1: EmbeddedObject) -> bool:
    return obj0._type() == obj1._type() and obj0.is_equal(obj1)

def equals_mod_360(scalar0: EmbeddedScalar, scalar1: EmbeddedScalar) -> bool:
    diff= (scalar0.value - scalar1.value) % 360
    return diff < EPSILON or 360 - diff < EPSILON
