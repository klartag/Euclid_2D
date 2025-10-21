from dataclasses import dataclass


from .abstract_term import AbstractTerm

@dataclass
class ConstantTerm[T](AbstractTerm[T]):
    value: T
