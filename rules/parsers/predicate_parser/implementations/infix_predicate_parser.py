from dataclasses import dataclass
import re
from typing import Optional

from ....expression_parse_utils import split_args
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import predicate_from_args

from ...abstract_recursive_geometry_parser import AbstractRecursiveGeometryParser


@dataclass
class InfixPredicateParser(AbstractRecursiveGeometryParser[Predicate, None, GeoObject]):
    """
    TODO: Document
    """

    predicate_name: str
    infix: str
    suffix: Optional[str] = None
    allow_multiple_arguments: bool = False

    def _try_split_components(self, text: str) -> Optional[tuple[None, tuple[str, ...]]]:
        regex = self.get_regex_matcher()
        match = re.fullmatch(regex, text)
        if match is None:
            return None
        components_text = match.groups()
        components_text = tuple([component_text.strip() for component_text in components_text])
        if self.allow_multiple_arguments:
            components_text = [
                subcomponent_text.strip()
                for component_text in components_text
                for subcomponent_text in split_args(component_text)
            ]

        return (None, components_text)

    def _build(self, _: None, components: tuple[GeoObject, ...]):
        return predicate_from_args(self.predicate_name, components)

    def get_regex_matcher(self):
        """
        TODO: Document
        """
        if self.suffix is None:
            return f"(.*){self.infix}(.*)"
        else:
            return F"(.*){self.infix}(.*){self.suffix}"
