from typing import Optional

from ...predicates.predicate import Predicate
from ...geometry_objects.geo_type import Signature

from ..abstract_geometry_parser import AbstractGeometryParser
from ..geometry_object_parser.geometry_object_parser import GeometryObjectParser

from .implementations.function_predicate_parser import FunctionPredicateParser
from .implementations.infix_predicate_parser import InfixPredicateParser


class PredicateParser(AbstractGeometryParser[Predicate]):
    signature: Signature
    parsers: list[AbstractGeometryParser[Predicate]]

    def __init__(self, signature: Signature):
        geometry_object_parsing_func = GeometryObjectParser(signature).try_parse

        self.signature = signature
        self.parsers = [
            InfixPredicateParser(geometry_object_parsing_func, 'equals', '=='),
            InfixPredicateParser(geometry_object_parsing_func, 'not_equals', '!='),
            InfixPredicateParser(geometry_object_parsing_func, 'equals_mod_360', '==', ' mod 360'),
            InfixPredicateParser(geometry_object_parsing_func, 'not_equals_mod_360', '!=', ' mod 360'),
            InfixPredicateParser(geometry_object_parsing_func, 'in', ' in ', allow_multiple_arguments=True),
            InfixPredicateParser(geometry_object_parsing_func, 'not_in', ' not in ', allow_multiple_arguments=True),
            FunctionPredicateParser(geometry_object_parsing_func),
        ]

    def try_parse(self, text: str) -> Optional[Predicate]:
        for parser in self.parsers:
            predicate = parser.try_parse(text)
            if predicate is not None:
                return predicate
        raise Exception("cannot none")
        return None
