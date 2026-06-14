from abc import abstractmethod
from typing import Iterator, Optional, Self

from fractions import Fraction

from .abstract_vector import AbstractVector

class AbstractIterableVector(AbstractVector):
    """A vector whose contents can be interated over, in a consistent order."""

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, i: int) -> Fraction: ...
    
    @abstractmethod
    def __setitem__(self, i: int, value: Fraction): ...

    @abstractmethod
    def extend_length(self, amount: int):
        """
        Makes the vector longer by `amount`.
        The new items in the vector will have the value 0.
        """
        ...

    @abstractmethod
    def permute(self, permutation: list[int]) -> Self:
        """
        Returns a vector `vector` of the same type that satisfies
        vector[i] = self[permutation[i]]
        
        permutation:    A list containing each integer from 0 up to `len(self) - 1`, once.
        """
        ...

    def __iter__(self) -> Iterator[Fraction]:
        return (self[i] for i in range(len(self)))

    @abstractmethod
    def first_nonzero_index(self) -> Optional[int]:
        ...

    @abstractmethod
    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        ...

    def __bool__(self) -> bool:
        return self.first_nonzero_index() is not None

    @abstractmethod
    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        """
        Returns the sum of absolute values of the items in the vector.
        If `max_index` is specified, only sums up to that index (not inclusive).
        """
        ...
    
    @classmethod
    @abstractmethod
    def create_empty(cls: type[Self], length: int) -> Self:
        """Creates a vector of length `length` of this class, where all values are zero."""
        ...
    
    @classmethod
    @abstractmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self:
        """
        Creates a vector of length `length` of this class,
        where all values are 0 except for the value an index `index`, which will equal 1.
        """
        ...
