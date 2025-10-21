from dataclasses import dataclass

from .abstract_input_equation import AbstractInputEquation


@dataclass
class SimpleEquation[T](AbstractInputEquation[T]):
    '''
    Represents an equation of the form `a = b`,
    where `a` is held in `left`,
    and `b` is held in `right`.
    '''

    left: T
    right: T
