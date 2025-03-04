import itertools
from typing import DefaultDict, Iterator, KeysView, List, Optional, ItemsView, Self, Tuple, ValuesView

from mpmath import mpf
from collections import defaultdict

from ..rule_utils import LITERAL
from ..predicates.predicate import Predicate

from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.construction_object import ConstructionObject
from ..geometry_objects.equation_object import EquationObject
from ..geometry_objects.eq_op import EqOp

from .method_dictionaries import CONSTRUCTION_METHOD_DICTIONARY, PREDICATE_METHOD_DICTIONARY

from .embedded_objects import EmbeddedObject, EmbeddedScalar
from .embedded_predicate_value import EmbeddedPredicateValue
from .undefined_embedding_error import UndefinedEmbeddingError


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
    
    def evaluate_object(self, obj: GeoObject) -> Tuple[EmbeddedObject, ...]:
        if obj.name in self.embedding:
            return (self.embedding[obj.name],)
        elif isinstance(obj, ConstructionObject):
            return self.evaluate_construction_object(obj)
        elif isinstance(obj, EquationObject):
            return self.evaluate_equation_object(obj)
        elif obj.type == LITERAL:
            return (EmbeddedScalar(mpf(obj.name)),)
        else:
            raise UndefinedEmbeddingError()
    
    def evaluate_construction_object(self, obj: ConstructionObject) -> Tuple[EmbeddedObject, ...]:
        if obj.constructor.name not in CONSTRUCTION_METHOD_DICTIONARY:
            raise UndefinedEmbeddingError(f'Unknown construction name: {obj.constructor.name}')
        construction_method = CONSTRUCTION_METHOD_DICTIONARY[obj.constructor.name]
        embedded_parameter_options: List[Tuple[EmbeddedObject, ...]] = []
        for component in obj.components:
            parameter_options = self.evaluate_object(component)
            embedded_parameter_options.append(parameter_options)
        return tuple(itertools.chain(*[construction_method(*parameters) for parameters in itertools.product(*embedded_parameter_options)]))

    def evaluate_equation_object(self, eqn: EquationObject) -> Tuple[EmbeddedScalar]:
        lhs_options = self.evaluate_object(eqn.left)
        rhs_options = self.evaluate_object(eqn.right)

        for lhs in lhs_options:
            if not isinstance(lhs, EmbeddedScalar):
                raise UndefinedEmbeddingError(f"Cannot evaluate an arithmetic expression with {lhs}, as it is not a scalar.")

        for rhs in rhs_options:
            if not isinstance(rhs, EmbeddedScalar):
                raise UndefinedEmbeddingError(f"Cannot evaluate an arithmetic expression with {rhs}, as it is not a scalar.")
            
        results = []

        for lhs in lhs_options:
            for rhs in rhs_options:
                match eqn.op:
                    case EqOp.ADD: results.append(lhs + rhs)
                    case EqOp.SUB: results.append(lhs - rhs)
                    case EqOp.MUL: results.append(lhs * rhs)
                    case EqOp.DIV: results.append(lhs / rhs)
                    case _: raise UndefinedEmbeddingError(f"Cannot evaluate an arithmetic expression with {eqn.op} as an operator.")

        return tuple(results)

    def evaluate_predicate(self, predicate: Predicate) -> EmbeddedPredicateValue:
        if predicate.name in PREDICATE_METHOD_DICTIONARY:
            predicate_method = PREDICATE_METHOD_DICTIONARY[predicate.name]
            embedded_parameter_options: List[Tuple[EmbeddedObject, ...]] = []
            for component in predicate.components:
                try:
                    parameter_options = self.evaluate_object(component)
                    embedded_parameter_options.append(parameter_options)
                except UndefinedEmbeddingError:
                    return EmbeddedPredicateValue.Undefined
            results = [predicate_method(*parameters) for parameters in itertools.product(*embedded_parameter_options)]
            if all(results):
                return EmbeddedPredicateValue.Correct
            else:
                ### TODO: What if *some* of the results are correct, and some aren't?
                ### TODO: Can we give partial results even if some objects are undefined? (instead of raising an error, return an empty tuple?)
                return EmbeddedPredicateValue.Incorrect
        else:
            raise Exception(f'Predicate {predicate.name} not recognized.')
