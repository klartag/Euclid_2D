from enum import Enum


class EqOp(Enum):
    '''An enum describing the type of mathematical operations that can be done to two Scalar objects.'''

    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

    def priority(self) -> int:
        """
        Returns an integer, representing which operation has precedence over which.
        A higher value has higher precedence.
        """
        match self:
            case EqOp.ADD | EqOp.SUB:
                return 1
            case EqOp.MUL | EqOp.DIV:
                return 2
