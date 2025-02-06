from typing import DefaultDict, Iterator, KeysView, Optional, ItemsView, Self, ValuesView

from mpmath import mpf
from collections import defaultdict

from ..rule_utils import LITERAL
from ..predicates.predicate import Predicate

from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.construction_object import ConstructionObject
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.eq_op import EqOp

from .constructions import CONSTRUCTION_METHOD_DICTIONARY
from .predicates import PREDICATE_METHOD_DICTIONARY
from .embedded_objects import EmbeddedObject, EmbeddedScalar


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
    
    def evaluate_object(self, obj: GeoObject) -> Optional[EmbeddedObject]:
        if obj.name in self.embedding:
            return self.embedding[obj.name]
        elif isinstance(obj, ConstructionObject):
            return self.evaluate_construction_object(obj)
        elif isinstance(obj, EquationObject):
            return self.evaluate_equation_object(obj)
        elif obj.type == LITERAL:
            return EmbeddedScalar(mpf(obj.name))
        else:
            return None
    
    def evaluate_construction_object(self, obj: ConstructionObject) -> Optional[EmbeddedObject]:
        if obj.constructor.name not in CONSTRUCTION_METHOD_DICTIONARY:
            return None
        construction_method = CONSTRUCTION_METHOD_DICTIONARY[obj.constructor.name]
        embedded_parameters = []
        for component in obj.components:
            embedded_component = self.evaluate_object(component)
            if embedded_component is None:
                return
            embedded_parameters.append(embedded_component)
        return construction_method(*embedded_parameters)

    def evaluate_equation_object(self, eqn: EquationObject) -> Optional[EmbeddedScalar]:
        lhs = self.evaluate_object(eqn.left)
        rhs = self.evaluate_object(eqn.right)
        
        if not isinstance(lhs, EmbeddedScalar) or not isinstance(rhs, EmbeddedScalar):
            return None
        
        match eqn.op:
            case EqOp.ADD: return EmbeddedScalar(lhs.value + rhs.value)
            case EqOp.SUB: return EmbeddedScalar(lhs.value - rhs.value)
            case EqOp.MUL: return EmbeddedScalar(lhs.value * rhs.value)
            case EqOp.DIV: return EmbeddedScalar(lhs.value / rhs.value)
            case _: return None

    def evaluate_predicate(self, predicate: Predicate) -> Optional[bool]:
        if predicate.name in PREDICATE_METHOD_DICTIONARY:
            predicate_method = PREDICATE_METHOD_DICTIONARY[predicate.name]
            embedded_parameters = []
            for component in predicate.components:
                parameter = self.evaluate_object(component)
                if parameter is None:
                    return None
                embedded_parameters.append(parameter)
            return predicate_method(*embedded_parameters)
        else:
            return None
