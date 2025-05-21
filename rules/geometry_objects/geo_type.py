from enum import Enum


class GeoType(Enum):
    SCALAR = 'Scalar'
    POINT = 'Point'
    LINE = 'Line'
    ANGLE = 'Angle'
    ORIENTATION = 'Orientation'
    LITERAL = 'Literal'
    CIRCLE = 'Circle'


R_EQN_TYPES = (GeoType.SCALAR, GeoType.ANGLE)
EQN_TYPES = (GeoType.SCALAR, GeoType.ANGLE, GeoType.LITERAL, GeoType.ORIENTATION)
