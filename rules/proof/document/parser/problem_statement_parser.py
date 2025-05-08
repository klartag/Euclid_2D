import re

from ....rule_utils import ALL_TYPES, ProofParseError
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import parse_predicate

from .proof_parser.step_parsers.object_definition_step_parser import (
    OBJECT_DEFINITION_PATTERN,
    OBJECT_NAME_PATTERN,
)


class ProblemStatementParser:
    def parse_assumptions(self, data: list[str]) -> tuple[dict[str, GeoObject], list[Predicate]]:
        """
        Parses the assumptions segment of the proof.
        Returns a proof with only the assumptions.
        """
        assumptions = []
        obj_map = {}
        # Parsing the assumptions section
        for line in self.preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                self.parse_object_definition_line(line, obj_map)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, obj_map)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof assumptions!')
                assumptions.append(pred)

        return obj_map, assumptions

    def parse_targets(
        self, data: list[str], obj_map: dict[str, GeoObject]
    ) -> tuple[dict[str, GeoObject], list[Predicate]]:
        """
        Parses the targets section of the proof.
        @return: A proof with an updated object map and only the target predicates set.
        """
        old_objects = dict(obj_map)
        target_predicates = []
        # Parsing the target section.
        for line in self.preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                self.parse_object_definition_line(line, obj_map)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, obj_map)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof targets!')

                target_predicates.append(pred)

        target_objects = {k: v for k, v in obj_map.items() if k not in old_objects}

        return target_objects, target_predicates

    def parse_object_definition_line(self, line: str, obj_map: dict[str, GeoObject]):
        """
        Parses a line defining objects.
        @param line: The line. Should be of the format a, b, c: Type
        """
        names, type_ = line.strip().split(':')
        type_ = type_.strip()

        if type_ not in ALL_TYPES:
            if re.fullmatch(OBJECT_DEFINITION_PATTERN, line):
                raise ProofParseError(
                    f'Illegal object definition: "{line}". Perhaps the line should be in the proof body?'
                )
            else:
                raise ProofParseError(f'Illegal type: "{type_}" in line "{line}".')

        for name in names.split(','):
            name = name.strip()
            if not re.fullmatch(OBJECT_NAME_PATTERN, name):
                raise ProofParseError(f'Illegal object name: "{name}"')
            if name in obj_map:
                raise ProofParseError(f'Object {name} redefined in line {line}!')

            obj_map[name] = GeoObject(name, type_)
