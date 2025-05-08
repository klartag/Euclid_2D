import json
import re
from typing import Iterable

from ....embeddings.embedded_objects.circle import EmbeddedCircle
from ....embeddings.embedded_objects.line import EmbeddedLine
from ....embeddings.embedded_objects.point import EmbeddedPoint
from ....embeddings.embedded_objects.scalar import EmbeddedScalar
from ....embeddings.embedding import Embedding
from ....geometry_objects.parse import parse_geo_object
from ....rule_utils import ProofParseError, split_args
from ....theorem import Theorem
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import parse_predicate, predicate_from_args

from ... import Proof

from ...steps.almost_always_step import AlmostAlwaysStep
from ...steps.assert_step import AssertStep
from ...steps.comment_step import CommentStep
from ...steps.null_theorem_step import NullTheoremStep
from ...steps.object_define_step import ObjDefineStep
from ...steps.step import Step
from ...steps.theorem_step import TheoremStep

from .. import rule_utils


class DocumentParser:
    def parse(self, data: str, parse_proof_body: bool = True) -> 'Proof':
        """
        Parses a string representing a proof.
        """
        lines = data.splitlines()
        stripped_lines = [line.strip() for line in lines]

        if (
            ASSUMPTION_TITLE not in stripped_lines
            or TARGET_TITLE not in stripped_lines
            or BODY_TITLE not in stripped_lines
        ):
            raise ProofParseError(
                f'Error when parsing proof: Missing section title.\nProof:{LINE_BREAK.join(stripped_lines)}'
            )

        end = len(stripped_lines)
        assumption_idx = stripped_lines.index(ASSUMPTION_TITLE) if ASSUMPTION_TITLE in stripped_lines else end
        target_idx = stripped_lines.index(TARGET_TITLE) if TARGET_TITLE in stripped_lines else end
        proof_idx = stripped_lines.index(BODY_TITLE) if BODY_TITLE in stripped_lines else end
        embed_idx = stripped_lines.index(EMBED_TITLE) if EMBED_TITLE in stripped_lines else end
        indices = sorted(list(set([end, end + 1, assumption_idx, target_idx, proof_idx, embed_idx])))

        assumption_end = indices[indices.index(assumption_idx) + 1]
        embed_end = indices[indices.index(embed_idx) + 1]
        target_end = indices[indices.index(target_idx) + 1]
        proof_end = indices[indices.index(proof_idx) + 1]

        if not 0 <= assumption_idx < target_idx < proof_idx < len(lines):
            raise ProofParseError(f'Section titles in proof are illegal: {assumption_idx=} {target_idx=} {proof_idx=}')

        assumption_lines = lines[assumption_idx + 1 : assumption_end]
        target_lines = lines[target_idx + 1 : target_end]
        proof_lines = lines[proof_idx + 1 : proof_end]
        embed_lines = lines[embed_idx + 1 : embed_end]

        assumption_objects, assumption_preds = self.parse_assumptions(assumption_lines)
        target_objects, target_preds = self.parse_targets(target_lines, dict(assumption_objects))
        auxiliary_preds: list[Predicate] = []

        exist_objects: set[GeoObject] = set()

        # Marking objects in the 'Assumptions' and in the 'Need To Prove' sections as existing.
        for obj in set(assumption_objects.values()) | set(target_objects.values()):
            exist_objects.add(obj)

        # Marking objects in predicates from the 'Assumptions' and 'Need To Prove' sections as existing.
        for pred in assumption_preds + target_preds:
            for obj in pred.involved_objects():
                exist_objects.add(obj)

        auxiliary_preds.append(predicate_from_args('exists', tuple(exist_objects)))

        steps = self.parse_body(proof_lines, dict(assumption_objects)) if parse_proof_body else []

        embedding = self.parse_embeds(embed_lines, assumption_objects) if len(embed_lines) > 0 else None

        return Proof(
            assumption_objects | target_objects,
            assumption_objects,
            assumption_preds,
            auxiliary_preds,
            target_objects,
            target_preds,
            embedding,
            steps,
        )

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

    def remove_comments(self, lines: Iterable[str]) -> Iterable[str]:
        """
        Removes comments from the lines and removes empty lines.
        """
        for line in lines:
            if '#' in line:
                line = line.split('#')[0]
            line = line.rstrip()
            if len(line) > 0:
                yield line

    def parse_object_definition_line(self, line: str, obj_map: dict[str, GeoObject]):
        """
        Parses a line defining objects.
        @param line: The line. Should be of the format a, b, c: Type
        """
        names, type_ = line.strip().split(':')
        type_ = type_.strip()

        if type_ not in ALL_TYPES:
            if re.fullmatch(OBJ_DEFINE_PATTERN, line):
                raise ProofParseError(
                    f'Illegal object definition: "{line}". Perhaps the line should be in the proof body?'
                )
            else:
                raise ProofParseError(f'Illegal type: "{type_}" in line "{line}".')

        for name in names.split(','):
            name = name.strip()
            if not re.fullmatch(OBJ_NAME_PATTERN, name):
                raise ProofParseError(f'Illegal object name: "{name}"')
            if name in obj_map:
                raise ProofParseError(f'Object {name} redefined in line {line}!')

            obj_map[name] = GeoObject(name, type_)

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

    def parse_embeds(self, data: list[str], obj_map: dict[str, GeoObject]) -> Embedding:
        """
        Parses the embedding section of the proof.
        """
        embedding = Embedding()
        for line in data:
            if not line.strip():
                continue
            name, data = line.split(':=')
            name = name.strip()
            data = json.loads(data)
            if name not in obj_map:
                raise ProofParseError(f'Embed given for unknown object: {name}')
            embedded_object = None
            match obj_map[name].type:
                case rule_utils.POINT:
                    embedded_object = EmbeddedPoint.from_dict(data)
                case rule_utils.LINE:
                    embedded_object = EmbeddedLine.from_dict(data)
                case rule_utils.CIRCLE:
                    embedded_object = EmbeddedCircle.from_dict(data)
                case rule_utils.ANGLE | rule_utils.SCALAR:
                    embedded_object = EmbeddedScalar.from_dict(data)

            embedding[name] = embedded_object

        return embedding
