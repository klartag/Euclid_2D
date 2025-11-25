from typing import Callable, Iterable

from .box import Box
from .union_find import UnionFind


class LabelledUnionFind[T, L](UnionFind[T]):
    """
    A disjoint-set-union data structure.
    """

    labels: dict[T, L]
    default_label_factory: Callable[[T], L]
    merge_label_factory: Callable[[T, L, T, L], L]
    
    def __init__(
        self,
        default_label_factory: Callable[[T], L],
        merge_label_factory: Callable[[T, L, T, L], L]
    ):
        super().__init__()
        self.labels = {}
        self.default_label_factory = default_label_factory
        self.merge_label_factory = merge_label_factory
        
    def get_label(self, obj: T) -> L:
        representative = self[obj]
        if representative not in self.labels:
            self.labels[representative] = self.default_label_factory(representative)
        return self.labels[representative]
    
    def delete_label(self, obj: T):
        representative = self[obj]
        if representative in self.labels:
            del self.labels[representative]
            
    def set_label(self, obj: T, label: L):
        self.labels[self[obj]] = label

    def __setitem__(self, key: T, value: T):
        """
        Sets `key` and `value` to be equal in the `UnionFind`.
        If required, changes the representative of `key` into the representative of `value`.
        """
        key_label = self.get_label(key)
        value_label = self.get_label(value)
        new_label = self.merge_label_factory(key, key_label, value, value_label)
        
        self.delete_label(key)
        self.delete_label(value)

        super()[key] = value
        
        self.set_label(key, new_label)

    def shallow_copy(self) -> 'LabelledUnionFind[T, L]':
        """
        Returns a shallow copy of the union-find:
        The structures of the union-find are copied, but all underlying objects are not.
        """
        res = LabelledUnionFind(self.default_label_factory, self.merge_label_factory)
        base_shallow_copy = super().shallow_copy()
        res.to_representative = base_shallow_copy.to_representative
        res.equivalences = base_shallow_copy.equivalences
        res.labels = {obj: label for (obj, label) in self.labels.items()}
        return res
