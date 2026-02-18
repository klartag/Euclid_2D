from enum import Enum


class GeoType(Enum):
    '''An enum representing the types of objects that might exist in a geometry problem.'''

    SCALAR = 'Scalar'
    POINT = 'Point'
    LINE = 'Line'
    ANGLE = 'Angle'
    ORIENTATION = 'Orientation'
    LITERAL = 'Literal'
    CIRCLE = 'Circle'


R_EQN_TYPES = (GeoType.SCALAR, GeoType.ANGLE)
# TODO: Document
EQN_TYPES = (GeoType.SCALAR, GeoType.ANGLE, GeoType.LITERAL, GeoType.ORIENTATION)
'''The types of objects that can be parameters of an EquationObject.'''

Signature = dict[str, GeoType]
'''Represents a mapping that describes, for each named object, what its type is.'''
