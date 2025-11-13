from typing import Hashable, List, Sequence, TypeVar 

T = TypeVar('T', bound=Hashable)

class IndexedSet[T]:
    values: list[T]
    reverse_key_dict: dict[T, int]
    
    def __init__(self, *values: T):
        self.values = list(values)
        self.reverse_key_dict = {self.values[i]: i for i in range(len(self.values))}
        
    def add(self, value: T) -> bool:
        if value in self:
            return False
        self.reverse_key_dict[value] = len(self.values)
        self.values.append(value)
        return True
            
    def __contains__(self, value: T) -> bool:
        return value in self.reverse_key_dict
    
    def index(self, value: T) -> int:
        return self.reverse_key_dict[value]

    def __getitem__(self, index: int) -> T:
        return self.values[index]

    def clone(self) -> 'IndexedSet[T]':
        return IndexedSet(*self.values)

    def __str__(self) -> str:
        return f'IndexedSet{self.values}'
