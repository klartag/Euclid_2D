import re
from typing import Mapping, NamedTuple

from rules.proof.document.document_section import DocumentSection
from rules.proof.document.geometry_document import GeometryDocument
from rules.proof.statement import Statement

from ....rule_utils import ALL_TYPES, ProofParseError, preprocess_lines
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import parse_predicate, predicate_from_args

from .proof_reader.step_readers.object_definition_step_reader import (
    OBJECT_DEFINITION_PATTERN,
    OBJECT_NAME_PATTERN,
)

PredicateData = NamedTuple('PredicateData', [("objects", dict[str, GeoObject]), ("predicates", list[Predicate])])


class ProblemStatementReader:
    def read(self, document: GeometryDocument) -> Statement:
        assumption_predicate_data = self.read_assumptions(document.get_section_text(DocumentSection.ASSUMPTION))
        target_predicate_data = self.read_targets(
            document.get_section_text(DocumentSection.TARGET), assumption_predicate_data.objects
        )
        auxiliary_predicates = self.create_auxiliary_predicates(assumption_predicate_data, target_predicate_data)

        return Statement(
            assumption_predicate_data.objects,
            assumption_predicate_data.predicates,
            auxiliary_predicates,
            target_predicate_data.objects,
            target_predicate_data.predicates,
        )

    def create_auxiliary_predicates(
        self, assumption_data: PredicateData, target_data: PredicateData
    ) -> list[Predicate]:
        auxiliary_preds: list[Predicate] = []

        exist_objects: set[GeoObject] = set(assumption_data.objects.values()) | set(target_data.objects.values())

        # Marking objects in predicates from the 'Assumptions' and 'Need To Prove' sections as existing.
        for pred in assumption_data.predicates + target_data.predicates:
            exist_objects |= pred.involved_objects()

        auxiliary_preds.append(predicate_from_args('exists', tuple(exist_objects)))

        return auxiliary_preds

    def read_assumptions(self, data: list[str]) -> PredicateData:
        """
        Parses the assumptions segment of the proof.
        Returns a proof with only the assumptions.
        """
        assumption_objects = {}
        assumption_predicates = []
        # Parsing the assumptions section
        for line in preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                self.read_object_definition_line(line, assumption_objects)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, assumption_objects)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof assumptions!')
                assumption_predicates.append(pred)

        return PredicateData(assumption_objects, assumption_predicates)

    def read_targets(self, data: list[str], assumption_objects: Mapping[str, GeoObject]) -> PredicateData:
        """
        Parses the targets section of the proof.
        @return: A proof with an updated object map and only the target predicates set.
        """
        old_objects = dict(assumption_objects)
        target_predicates = []
        # Parsing the target section.
        for line in preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                self.read_object_definition_line(line, assumption_objects)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, assumption_objects)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof targets!')

                target_predicates.append(pred)

        target_objects = {k: v for k, v in assumption_objects.items() if k not in old_objects}

        return PredicateData(target_objects, target_predicates)

    def read_object_definition_line(self, line: str, assumption_objects: Mapping[str, GeoObject]):
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
            if name in assumption_objects:
                raise ProofParseError(f'Object {name} redefined in line {line}!')

            assumption_objects[name] = GeoObject(name, type_)
