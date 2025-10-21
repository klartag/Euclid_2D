from dataclasses import dataclass

from .abstract_input_equation import AbstractInputEquation


@dataclass
class FunctionalEquation[T](AbstractInputEquation[T]):
    '''
    Represents an equation of the form `F(a_1, a_2, ..., a_n) = b`.
    Where `F` is held in `function`,
    `a_1, a_2, ..., a_n` is held in `left`,
    and `b` is held in `right`.
    '''

    function: str
    left: list[T]
    right: T
