from typing import Callable, Tuple, Union, Unpack

from .embedded_objects.embedded_object import EmbeddedObject


ExtendedConstructionMethod = Callable[
    [Unpack[Tuple[EmbeddedObject, ...]]], Union[EmbeddedObject, Tuple[EmbeddedObject, ...]]
]
# TODO: Document
ConstructionMethod = Callable[[Unpack[Tuple[EmbeddedObject, ...]]], Tuple[EmbeddedObject, ...]]
# TODO: Document
PredicateMethod = Callable[[Unpack[Tuple[EmbeddedObject, ...]]], bool]
# TODO: Document

def normalize_return_type(func: ExtendedConstructionMethod) -> ConstructionMethod:
    # TODO: Document
    def wrapper(*parameters: Tuple[EmbeddedObject, ...]) -> Tuple[EmbeddedObject, ...]:
        construction_result = func(*parameters)
        if isinstance(construction_result, EmbeddedObject):
            return (construction_result,)
        else:
            return construction_result

    wrapper.__name__ = f'normalized_{func.__name__}'
    return wrapper
