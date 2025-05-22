from dataclasses import dataclass
import re
from typing import Optional
from rules.expression_parse_utils import split_args
from rules.geometry_objects.geo_object import GeoObject
from rules.parsers.abstract_recursive_geometry_parser import AbstractRecursiveGeometryParser
from rules.predicates.predicate import Predicate
from rules.predicates.predicate_factory import predicate_from_args


@dataclass
class FunctionPredicateParser(AbstractRecursiveGeometryParser[Predicate, str, GeoObject]):
    def _try_split_components(self, text: str) -> Optional[tuple[str, tuple[str, ...]]]:
        if '(' not in text:
            return None
        if text[-1] != ')':
            return None

        predicate_name, argument_string = text[:-1].split('(', 1)

        arguments = split_args(argument_string)
        if arguments is None:
            return None
        return (predicate_name, tuple(arguments))

    def _build(self, data: str, components: tuple[GeoObject, ...]):
        return predicate_from_args(data, components)
