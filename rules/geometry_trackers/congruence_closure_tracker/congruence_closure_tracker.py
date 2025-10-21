from .input_equations.simple_equation import SimpleEquation
from .input_equations.functional_equation import FunctionalEquation

class CongruenceClosureTracker[T]:
    pending: list[SimpleEquation[T] | tuple[FunctionalEquation[T], FunctionalEquation[T]]]
    representatives: dict[T, T]
    class_lists: dict[T, list[T]]
    use_lists: dict[T, list[FunctionalEquation[T]]]
    lookup_table: dict[tuple[T, T], FunctionalEquation[T]]
