from typing import Optional
from rules.geometry_objects.geo_type import Signature
from rules.parsers.abstract_geometry_parser import AbstractGeometryParser
from rules.parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from rules.predicates.predicate import Predicate


class PredicateParser(AbstractGeometryParser[Predicate]):
    parsers: list[AbstractGeometryParser[Predicate]]

    def __init__(self, signature: Signature):
        geometry_object_parser = GeometryObjectParser(signature)

        self.parsers = []

    def try_parse(self, text: str) -> Optional[Predicate]:
        for parser in self.parsers:
            predicate = parser.try_parse(text)
            if predicate is not None:
                return predicate
        return None
