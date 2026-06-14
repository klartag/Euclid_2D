from ..embedded_objects import EmbeddedObject, EmbeddedScalar, EPSILON


def equals(obj0: EmbeddedObject, obj1: EmbeddedObject) -> bool:
    """
    Checks whether two objects are equal.
    """
    return obj0._type() == obj1._type() and obj0.is_equal(obj1)


def not_equals(obj0: EmbeddedObject, obj1: EmbeddedObject) -> bool:
    """
    Checks whether two objects are different.
    """
    return not equals(obj0, obj1)


def equals_mod_360(scalar0: EmbeddedScalar, scalar1: EmbeddedScalar) -> bool:
    """
    Checks whether two scalars are equal mod 360.
    """
    diff= (scalar0.value - scalar1.value) % 360
    return diff < EPSILON or 360 - diff < EPSILON


def not_equals_mod_360(scalar0: EmbeddedScalar, scalar1: EmbeddedScalar) -> bool:
    """
    Checks whether two scalars are different mod 360.
    """
    return not equals_mod_360(scalar0, scalar1)


def distinct(*objects: EmbeddedObject) -> bool:
    """
    Checks whether the objects in a list are pairwise-disjoint.
    """
    return all([not_equals(objects[i], objects[j]) for i in range(len(objects)) for j in range(i)])


def identical(*objects: EmbeddedObject) -> bool:
    """
    Checks whether all the objects in a list are identical.
    """
    return all([equals(objects[i], objects[i + 1]) for i in range(len(objects) - 1)])


def not_one_of(*objects: EmbeddedObject) -> bool:
    """
    Checks whether the first object in a list is different from all the others.
    """
    return all([not_equals(objects[0], objects[i]) for i in range(1, len(objects))])
