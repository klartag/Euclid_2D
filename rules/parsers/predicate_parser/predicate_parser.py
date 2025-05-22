from typing import Optional
from rules.geometry_objects.geo_type import Signature
from rules.parsers.abstract_geometry_parser import AbstractGeometryParser
from rules.parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from rules.parsers.predicate_parser.implementations.function_predicate_parser import FunctionPredicateParser
from rules.parsers.predicate_parser.implementations.infix_predicate_parser import InfixPredicateParser
from rules.predicates.predicate import Predicate


class PredicateParser(AbstractGeometryParser[Predicate]):
    parsers: list[AbstractGeometryParser[Predicate]]

    def __init__(self, signature: Signature):
        geometry_object_parsing_func = GeometryObjectParser(signature).try_parse

        self.parsers = [
            InfixPredicateParser(geometry_object_parsing_func, 'equals', '=='),
            InfixPredicateParser(geometry_object_parsing_func, 'not_equals', '!='),
            InfixPredicateParser(geometry_object_parsing_func, 'equals_mod_360', '==', ' mod 360'),
            InfixPredicateParser(geometry_object_parsing_func, 'not_equals_mod_360', '!=', ' mod 360'),
            InfixPredicateParser(geometry_object_parsing_func, 'in', ' in '),
            InfixPredicateParser(geometry_object_parsing_func, 'not_in', ' not in '),
            FunctionPredicateParser(geometry_object_parsing_func),
        ]

    def try_parse(self, text: str) -> Optional[Predicate]:
        for parser in self.parsers:
            predicate = parser.try_parse(text)
            if predicate is not None:
                return predicate
        return None
