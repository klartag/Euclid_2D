from enum import Enum


class EqOp(Enum):
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
