from dataclasses import dataclass


@dataclass
class Apply[A, B]:
    func: A
    parameter: B


@dataclass
class Equation[A, B]:
    lhs: A
    rhs: B
