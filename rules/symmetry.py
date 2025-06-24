from enum import Enum, auto
import itertools
from typing import TypeVar, Protocol


class Sortable(Protocol):
    """
    A bound for types that can be sorted.
    """

    def __lt__(self, other) -> bool: ...


T = TypeVar('T', bound=Sortable)


class Symmetry(Enum):
    """
    Represents a symmetry group of a list of objects.
    """

    NONE = auto()
    ALL = auto()  # The full permutation group.
    BETWEEN = auto()  # Flips the order of all objects.
    SWAP = auto()  # Swaps the last two objects.
    CYCLIC = auto()  # Performs cyclic shifts of the objects.
    CIRCLE_SYMMETRY = auto()  # cyclic + reflactions
    TRIANGLE_PERMUTRATION = auto()  # (O, {A, B, C})
    QUADRILATERAL_PERMUTATION = auto()  # (O, {A, B, C, D})
    TWOFOUR = auto()  # (O, A, B, C) == (O, C, B, A)
    PI_ROTATE = auto()  # (A, B, C, D) == (C, D, A, B)
    LAST_ELEMENTS = auto()  # (X_1, {X_2,....,X_n})
    LAST_ELEMENTS_CIRCLE_SYMMETRY = auto()  # cyclic + reflactions for all elments exapt the first
    DOUBLE_SWAP = auto()  # (A, B, A', B') == (B, A, B', A')
    TWO_SEGMENTS = auto()  # ({{A, B} , {A', B'}})
    CONGRUENCE_TRIANGLES = (
        auto()
    )  # abcxyz = acbxzy = bacyxz = bcayzx = cabzxy = cbazyx = xyzabc = xzyacb = yxzbac = yzxbca = zxycab = zyxcba

    def all_orders(self, inputs: tuple[T, ...]) -> list[tuple[T, ...]]:
        match self:
            case Symmetry.NONE:
                return [inputs]
            case Symmetry.ALL:
                return list(itertools.permutations(inputs))
            case Symmetry.LAST_ELEMENTS:
                last_inputs = inputs[1:]
                first_input = inputs[0]
                last_inputs_permutations = list(itertools.permutations(last_inputs))
                return [tuple([first_input]) + x for x in last_inputs_permutations]
            case Symmetry.BETWEEN:
                return [inputs, inputs[::-1]]
            case Symmetry.SWAP:
                A, B, C = inputs
                return [(A, B, C), (A, C, B)]
            case Symmetry.CYCLIC:
                return [inputs[i:] + inputs[:i] for i in range(len(inputs))]

            case Symmetry.CIRCLE_SYMMETRY:
                cycles = [tuple(inputs[i:] + inputs[:i]) for i in range(len(inputs))]
                oppiste_cycles = [tuple([cycle[len(cycle) - 1 - i] for i in range(len(cycle))]) for cycle in cycles]
                return cycles + oppiste_cycles

            case Symmetry.LAST_ELEMENTS_CIRCLE_SYMMETRY:
                last_inputs = inputs[1:]
                first_input = inputs[0]
                last_inputs_cycles = [tuple(last_inputs[i:] + last_inputs[:i]) for i in range(len(last_inputs))]
                last_inputs_oppiste_cycles = [cycle[::-1] for cycle in last_inputs_cycles]
                return [tuple([first_input]) + l for l in last_inputs_cycles + last_inputs_oppiste_cycles]

            case Symmetry.TRIANGLE_PERMUTRATION:
                O, A, B, C = inputs
                return [(O, t[0], t[1], t[2]) for t in itertools.permutations((A, B, C))]
            case Symmetry.QUADRILATERAL_PERMUTATION:
                O, A, B, C, D = inputs
                return [(O, t[0], t[1], t[2], t[3]) for t in itertools.permutations((A, B, C, D))]
            case Symmetry.TWOFOUR:
                O, A, B, C = inputs
                return [(O, A, B, C), (O, C, B, A)]
            case Symmetry.PI_ROTATE:
                A, B, C, D = inputs
                return [(A, B, C, D), (C, D, A, B)]
            case Symmetry.DOUBLE_SWAP:
                A, B, C, D = inputs
                return [(A, B, C, D), (B, A, D, C)]
            case Symmetry.TWO_SEGMENTS:
                A, B, C, D = inputs
                return [
                    (A, B, C, D),
                    (A, B, D, C),
                    (B, A, C, D),
                    (B, A, D, C),
                    (C, D, A, B),
                    (D, C, A, B),
                    (C, D, B, A),
                    (D, C, B, A),
                ]
            case Symmetry.CONGRUENCE_TRIANGLES:
                A, B, C, X, Y, Z = inputs
                return [
                    (A, B, C, X, Y, Z),
                    (A, C, B, X, Z, Y),
                    (B, A, C, Y, X, Z),
                    (B, C, A, Y, Z, X),
                    (C, A, B, Z, X, Y),
                    (C, B, A, Z, Y, X),
                    (X, Y, Z, A, B, C),
                    (X, Z, Y, A, C, B),
                    (Y, X, Z, B, A, C),
                    (Y, Z, X, B, C, A),
                    (Z, X, Y, C, A, B),
                    (Z, Y, X, C, B, A),
                ]

    def canonical_order(self, inputs: tuple[T, ...]) -> tuple[T, ...]:
        """
        Returns a unique representation of the inputs."""
        match self:
            case Symmetry.NONE:
                return inputs
            case Symmetry.ALL:
                return tuple(sorted(inputs))
            case _:
                return min(self.all_orders(inputs))

    @staticmethod
    def parse(data: str) -> 'Symmetry':
        """
        Parses the input symmetry. Currently just accepts a list of names.
        """
        match data.lower():
            case 'no' | 'none':
                return Symmetry.NONE
            case 'symmetric' | 'all':
                return Symmetry.ALL
            case 'last_elements':
                return Symmetry.LAST_ELEMENTS
            case 'last_elements_circle_symmetry':
                return Symmetry.LAST_ELEMENTS_CIRCLE_SYMMETRY
            case 'between':
                return Symmetry.BETWEEN
            case 'cyclic':
                return Symmetry.CYCLIC
            case 'swap':
                return Symmetry.SWAP

            case 'circle_symmetry':
                return Symmetry.CIRCLE_SYMMETRY
            case 'triangle_permutation':
                return Symmetry.TRIANGLE_PERMUTRATION
            case 'qudrilatral_permutation':
                return Symmetry.QUADRILATERAL_PERMUTATION
            case 'two_four':
                return Symmetry.TWOFOUR
            case 'pi_rotate':
                return Symmetry.PI_ROTATE
            case 'double_swap':
                return Symmetry.DOUBLE_SWAP
            case 'two_segments':
                return Symmetry.TWO_SEGMENTS
            case 'congruence_triangles':
                return Symmetry.CONGRUENCE_TRIANGLES
            case _:
                raise NotImplementedError(f'Unknown symmetry group: {data}!')
