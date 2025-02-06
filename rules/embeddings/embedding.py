from typing import DefaultDict, Iterator, KeysView, Optional, ItemsView, Self, ValuesView

from collections import defaultdict

from .embedded_objects import EmbeddedObject


class Embedding:
    embedding: DefaultDict[str, Optional[EmbeddedObject]]
    
    def __init__(self):
        self.embedding = defaultdict(lambda: None)

    def __setitem__(self, object_name: str, embedded_object: EmbeddedObject):
        self.embedding[object_name] = embedded_object

    def __getitem__(self, object_name: str) -> Optional[EmbeddedObject]:
        return self.embedding[object_name]
    
    def __contains__(self, object_name: str) -> bool:
        return object_name in self.embedding
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.embedding)
    
    def keys(self) -> KeysView[str]:
        return self.embedding.keys()
    
    def values(self) -> ValuesView[Optional[EmbeddedObject]]:
        return self.embedding.values()

    def items(self) -> ItemsView[str, Optional[EmbeddedObject]]:
        return self.embedding.items()

    def shallow_copy(self) -> Self:
        copied_embedding = Embedding()
        for object_name, embedded_object in self.items():
            copied_embedding[object_name] = embedded_object
        return copied_embedding
