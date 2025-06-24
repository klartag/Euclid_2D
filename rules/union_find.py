from typing import Generic, Iterable, TypeVar

T = TypeVar('T')


class Box(Generic[T]):
    """
    A class that is effectively just a pointer to an object.
    """

    inner: T

    def __init__(self, value: T):
        self.inner = value

    def __eq__(self, other: 'Box[T]'):
        return self.inner == other.inner


class UnionFind(Generic[T]):
    """
    A disjoint-set-union data structure.
    """

    to_representative: dict[T, Box[T]]
    equivalences: dict[T, set[T]]

    def __init__(self):
        self.to_representative = {}
        self.equivalences = {}

    def __getitem__(self, obj: T) -> T:
        """
        Gets a representative of the equivalence class of the given object.
        @param obj: Some object.
        @return: The representative of the equivalence class of the given object
        """
        if obj not in self.to_representative:
            self.to_representative[obj] = Box(obj)
            self.equivalences[obj] = {obj}

        return self.to_representative[obj].inner

    def __setitem__(self, key: T, value: T):
        """
        Sets `key` and `value` to be equal in the `UnionFind`.
        If required, changes the representative of `key` into the representative of `value`.
        """
        key_rep = self[key]
        value_rep = self[value]
        if key_rep == value_rep:
            return

        key_box = self.to_representative[key]
        value_box = self.to_representative[value]

        key_equivalences = self.equivalences[key_rep]
        value_equivalences = self.equivalences[value_rep]

        del self.equivalences[key_rep]

        if len(value_equivalences) < len(key_equivalences):
            key_equivalences, value_equivalences = value_equivalences, key_equivalences
            value_box, key_box = key_box, value_box
        for obj in key_equivalences:
            self.to_representative[obj] = value_box

        value_equivalences |= key_equivalences
        value_box.inner = value_rep
        self.equivalences[value_rep] = value_equivalences
        assert self[key] == value_rep

    def __contains__(self, key: T) -> bool:
        """
        Returns if the key is contained in the union-find tree.
        """
        return key in self.to_representative

    def all_objects(self) -> Iterable[T]:
        """
        TODO: Document
        """
        return self.to_representative.keys()

    def get_representatives(self) -> Iterable[T]:
        """
        TODO: Document
        """
        return self.equivalences.keys()

    def get_equivalences(self, key: T) -> set[T]:
        """
        TODO: Document
        """
        return self.equivalences.get(key, set())

    def shallow_copy(self) -> 'UnionFind[T]':
        """
        Returns a shallow copy of the union-find:
        The structures of the union-find are copied, but all underlying objects are not.
        """
        res = UnionFind()
        res.to_representative = {key: Box(val.inner) for key, val in self.to_representative.items()}
        res.equivalences = {key: set(val) for key, val in self.equivalences.items()}
        return res
