import abc
from collections import defaultdict
import dataclasses
from dataclasses import dataclass
from mpmath import mpf
import itertools
import json
from pathlib import Path
import random
import re
import string
from typing import Iterable, Mapping, Optional

from util import BASE_PATH

from . import rule_utils

from .rule_utils import ALL_TYPES, LITERAL, ProofParseError, split_args

from .embeddings import Embedding
from .embeddings.embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EmbeddedScalar
from .predicates.implementations.exists_predicate import ExistsPredicate
from .predicates.predicate_factory import parse_predicate, predicate_from_args
from .predicates.predicate import Predicate
from .geometry_objects.construction_object import ConstructionObject
from .geometry_objects.geo_object import GeoObject
from .geometry_objects.equation_object import EquationObject
from .geometry_objects.parse import parse_geo_object
from .theorem import Theorem

ASSUMPTION_TITLE = 'Assumptions:'
TARGET_TITLE = 'Need to prove:'
EMBED_TITLE = 'Embedding:'
BODY_TITLE = 'Proof:'

LINE_BREAK = '\n'

OBJ_NAME_PATTERN = r'([\w\']+)'
THEOREM_STEP_PATTERN = r'By (\w+)( on )?(.*) we get (.*)$'
NULL_THEOREM_STEP_PATTERN = r'We have (.*)$'
COMMENT_STEP_PATTERN = r'Comment: \w*(.*)'
OBJ_DEFINE_PATTERN = rf'Let {OBJ_NAME_PATTERN} := (.*)$'  # The pattern for naming new constructions.
"""The pattern for introducing new constructions."""
OBJ_DEFINE_PATTERN_2 = rf'We introduce (.*)$'
"""The pattern for introducing new constructions without naming them."""
ASSERT_PATTERN = r'We have (proved|shown) (.*)$'
ALMOST_ALWAYS_STEP = r'It is almost always true that (.*)$'
IF_PATTERN = r'(\s*)If (.*):$'
ELSE_IF_PATTERN = r'Else if (.*):$'


@dataclass
class Step(abc.ABC):
    @abc.abstractmethod
    def to_language_format(self) -> str:
        """
        Converts the given step to a string representing the step.
        """
        ...

    @abc.abstractmethod
    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        """
        Replaces the object in the given step with other objects.
        """
        ...


@dataclass
class NullTheoremStep(Step):
    result_objects: list[GeoObject]
    result_predicates: list[Predicate]

    def to_language_format(self) -> str:
        result_str = ', '.join(
            [f'{obj.name}: {obj.type}' for obj in self.result_objects]
            + [pred.to_language_format() for pred in self.result_predicates]
        )
        return f'We have {result_str}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return NullTheoremStep(
            [g.substitute(subs) for g in self.result_objects],
            [pred.substitute(subs) for pred in self.result_predicates],
        )


@dataclass
class CommentStep(Step):
    comment: str

    def to_language_format(self):
        return f'Comment: {self.comment}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return CommentStep(self.comment)


@dataclass
class TheoremStep(Step):
    theorem_name: str
    inputs: list[GeoObject]
    result_objects: list[GeoObject]
    result_predicates: list[Predicate]
    comment: str = dataclasses.field(compare=False, default='')

    def to_language_format(self) -> str:
        input_str = ', '.join(obj.name for obj in self.inputs)
        result_str = ', '.join(
            [obj.name for obj in self.result_objects] + [pred.to_language_format() for pred in self.result_predicates]
        )

        comment = f'  # {self.comment}' if self.comment else ''

        return f'By {self.theorem_name} on {input_str} we get {result_str}{comment}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return TheoremStep(
            self.theorem_name,
            [g.substitute(subs) for g in self.inputs],
            [g.substitute(subs) for g in self.result_objects],
            [pred.substitute(subs) for pred in self.result_predicates],
            self.comment,
        )

    def __hash__(self) -> int:
        return hash(self.theorem_name) ^ hash(tuple(self.inputs))


@dataclass
class ObjDefineStep(Step):
    """
    A step that defines a new object. Can be used either as:
    Let a := tangent(B, c)
    Or as:
    We introduce tangent(B, c)
    """

    left_hand: GeoObject
    right_hand: GeoObject | None = dataclasses.field(default=None)

    def to_language_format(self) -> str:
        if self.right_hand is not None:
            return f'Let {self.left_hand.name} := {self.right_hand.name}'
        else:
            return f'We introduce {self.left_hand.name}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return ObjDefineStep(
            self.left_hand.substitute(subs), self.right_hand.substitute(subs) if self.right_hand is not None else None
        )


@dataclass
class AssertStep(Step):
    """
    A step of the form:
    We have shown that A, B, C.
    """

    predicates: list[Predicate]

    def to_language_format(self) -> str:
        return f'We have shown ' + ', '.join(pred.to_language_format() for pred in self.predicates)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return AssertStep([pred.substitute(subs) for pred in self.predicates])


@dataclass
class IfStep(Step):
    """
    A step of the form:
    If predicate:
        stuff
    Else if predicate:
        stuff
    """

    data: dict[Predicate, list[Step]]
    """A dictionary, containing a map from tested predicate to the proof segment under it."""

    def to_language_format(self) -> str:
        reprs = [
            (pred.to_language_format(), '\n'.join(step.to_language_format() for step in steps))
            for pred, steps in self.data.items()
        ]
        reprs = sorted(reprs, key=lambda t: len(t[1]))
        res = []
        for pred, body in reprs:
            if len(res) == 0:
                res.append(f'If {pred}:')
            else:
                res.append(f'Else if {pred}:')
            body = body.split('\n')
            body = ['\t' + row for row in body]
            body = '\n'.join(body)
            res.append(body)
        return '\n'.join(res)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return IfStep(
            {
                pred.substitute(subs): [sub_step.substitute(subs) for sub_step in sub_steps]
                for pred, sub_steps in self.data.items()
            }
        )


@dataclass
class AlmostAlwaysStep(Step):
    """
    A step that states that some predicate is satisfied on an open set,
    and asserts that in the current problem it is almost always true.
    This assertion is not checked, and incorrect use of this step can lead to contradictions.
    """

    predicates: list[Predicate]

    def to_language_format(self) -> str:
        return f'It is almost always true that ' + ', '.join(pred.to_language_format() for pred in self.predicates)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return AlmostAlwaysStep([pred.substitute(subs) for pred in self.predicates])


class Proof:
    """
    A class representing a proof.
    Stores a list of involved objects and the theorems applied on them,
    while doing no verification.
    The format in which a proof is stored is detailed in the language specification document.
    """

    all_objects: dict[str, GeoObject]
    assumption_objects: dict[str, GeoObject]
    assumption_predicates: list[Predicate]
    auxiliary_predicates: list[Predicate]
    target_objects: dict[str, GeoObject]
    target_predicates: list[Predicate]
    embedding: Optional[Embedding]
    steps: list[Step]

    def __init__(
        self,
        objects: dict[str, GeoObject],
        assumption_objects: dict[str, GeoObject],
        assumption_predicates: list[Predicate],
        auxiliary_predicates: list[Predicate],
        target_objects: dict[str, GeoObject],
        target_predicates: list[Predicate],
        embedding: Optional[Embedding],
        steps: list[Step],
    ):

        self.all_objects = objects
        self.assumption_objects = assumption_objects
        self.assumption_predicates = assumption_predicates
        self.auxiliary_predicates = auxiliary_predicates
        self.target_objects = target_objects
        self.target_predicates = target_predicates
        self.embedding = embedding
        self.steps = steps

    @staticmethod
    def parse_object_definition_line(line: str, obj_map: dict[str, GeoObject]):
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

    @staticmethod
    def preprocess_lines(lines: Iterable[str]) -> Iterable[str]:
        """
        Removes comments from the lines and removes empty lines.
        """
        for line in lines:
            if '#' in line:
                line = line.split('#')[0]
            line = line.rstrip()
            if line:
                yield line

    @staticmethod
    def parse_assumptions(data: list[str]) -> tuple[dict[str, GeoObject], list[Predicate]]:
        """
        Parses the assumptions segment of the proof.
        Returns a proof with only the assumptions.
        """
        assumptions = []
        obj_map = {}
        # Parsing the assumptions section
        for line in Proof.preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                Proof.parse_object_definition_line(line, obj_map)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, obj_map)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof assumptions!')
                assumptions.append(pred)

        return obj_map, assumptions

    @staticmethod
    def parse_targets(data: list[str], obj_map: dict[str, GeoObject]) -> tuple[dict[str, GeoObject], list[Predicate]]:
        """
        Parses the targets section of the proof.
        @return: A proof with an updated object map and only the target predicates set.
        """
        old_objects = dict(obj_map)
        target_predicates = []
        # Parsing the target section.
        for line in Proof.preprocess_lines(data):
            if ':' in line:
                # Checking if the line contains object definitions.
                Proof.parse_object_definition_line(line, obj_map)
            else:
                # Parsing a predicate.
                pred = parse_predicate(line, obj_map)
                if not pred.is_valid():
                    raise ProofParseError(f'Found invalid predicate {pred} in proof targets!')

                target_predicates.append(pred)

        target_objects = {k: v for k, v in obj_map.items() if k not in old_objects}

        return target_objects, target_predicates

    @staticmethod
    def parse_body(lines: list[str], obj_map: dict[str, GeoObject]) -> list[Step]:
        """
        Parses the body of the proof.
        This step is used recursively when parsing if-steps.
        """
        lines = list(Proof.preprocess_lines(lines))
        steps = []

        line_idx = 0
        try:
            while line_idx < len(lines):
                line = lines[line_idx]
                line_idx += 1
                if (assert_match := re.search(ASSERT_PATTERN, line)) is not None:
                    # The assert pattern has the same prefix as the null theorem, so it must come first.
                    _, preds_text = assert_match.groups()
                    preds = [parse_predicate(part, obj_map) for part in split_args(preds_text)]
                    steps.append(AssertStep(preds))
                elif (assert_match := re.search(ALMOST_ALWAYS_STEP, line)) is not None:
                    # The assert pattern has the same prefix as the null theorem, so it must come first.
                    preds_text = assert_match.group(1)
                    preds = [parse_predicate(part, obj_map) for part in split_args(preds_text)]
                    steps.append(AlmostAlwaysStep(preds))
                elif (comment_match := re.search(COMMENT_STEP_PATTERN, line)) is not None:
                    comment = comment_match.group(1).strip()
                    steps.append(CommentStep(comment))
                elif (null_theorem_match := re.search(NULL_THEOREM_STEP_PATTERN, line)) is not None:
                    # Matching a theorem step without a defined theorem.
                    results = null_theorem_match.group(1)
                    results = split_args(results)

                    # Attempting to differentiate between results and predicates.
                    construct_count = 0

                    while construct_count < len(results):
                        if ':' not in results[construct_count]:
                            break
                        construct_count += 1

                    result_objects = []
                    for const in results[:construct_count]:
                        name, typ = const.split(':')
                        name = name.strip()
                        typ = typ.strip()
                        if name in obj_map:
                            raise ProofParseError(f'Object {name} defined twice!')
                        res_obj = GeoObject(name, typ)
                        result_objects.append(res_obj)
                        obj_map[name] = res_obj

                    result_predicates = [parse_predicate(result, obj_map) for result in results]

                    steps.append(NullTheoremStep(result_objects, result_predicates))

                elif (theorem_match := re.search(THEOREM_STEP_PATTERN, line)) is not None:
                    # Matching a theorem step using a named theorem.
                    name, _, args, results = theorem_match.groups()
                    args = split_args(args) if args else []
                    results = split_args(results)

                    if name not in Theorem.all_theorems():
                        raise ProofParseError(f'Proof used unknown theorem: {name} in line {line}!')
                    theorem = Theorem.all_theorems().get(name, None)
                    if theorem is None:
                        raise ProofParseError(f'In line {line}, theorem {name} is unknown!')

                    inputs = [parse_geo_object(arg.strip(), obj_map) for arg in args]
                    if len(inputs) > len(theorem.signature):
                        raise ProofParseError(f'In line {line}, too many arguments for theorem {name}!')
                    if len(inputs) < len(theorem.signature):
                        raise ProofParseError(f'In line {line}, too few arguments for theorem {name}!')

                    # The first outputs are objects constructed by the theorem.
                    # We make sure enough objects were constructed.
                    construct_names = results[: len(theorem.result_objects)]
                    if len(construct_names) < len(theorem.result_objects):
                        raise ProofParseError(f'In line {line}, not enough objects are built by the theorem!')

                    # Adding the constructed objects.
                    result_objects = []
                    for cons_name, theorem_out in zip(construct_names, theorem.result_objects):
                        if cons_name in obj_map:
                            raise ProofParseError(f'Line {line} redefines the object {cons_name}!')
                        typ = theorem_out.type
                        res = GeoObject(cons_name, typ)
                        obj_map[cons_name] = res
                        result_objects.append(res)

                    result_predicates = [
                        parse_predicate(result, obj_map) for result in results[len(theorem.result_objects) :]
                    ]
                    steps.append(TheoremStep(name, inputs, result_objects, result_predicates, ''))

                elif (obj_define_match := re.search(OBJ_DEFINE_PATTERN, line)) is not None:
                    left, right = obj_define_match.groups()
                    right_obj = parse_geo_object(right, obj_map)
                    left_obj = GeoObject(left, right_obj.type)
                    if left_obj.name in obj_map:
                        raise ProofParseError(f'Object {left_obj.name} redefined in line {line}!')

                    obj_map[left_obj.name] = left_obj
                    steps.append(ObjDefineStep(left_obj, right_obj))

                elif (obj_define_match := re.search(OBJ_DEFINE_PATTERN_2, line)) is not None:
                    obj = obj_define_match.group(1)
                    obj = parse_geo_object(obj, obj_map)
                    obj_map[obj.name] = obj
                    steps.append(ObjDefineStep(obj))

                elif (else_if_match := re.search(ELSE_IF_PATTERN, line)) is not None:
                    raise ProofParseError(f'Failed to parse proof: line {line} is an else-if without an if.')

                elif (if_match := re.search(IF_PATTERN, line)) is not None:
                    whitespace, pred = if_match.groups()
                    pred = parse_predicate(pred, obj_map)
                    block_lines = []

                    pred_dict = {}

                    while line_idx <= len(lines):
                        # Checking if the block has ended.
                        if (
                            (line_idx == len(lines))
                            or (len(lines[line_idx]) <= len(whitespace))
                            or (not lines[line_idx][len(whitespace)].isspace())
                        ):
                            pred_dict[pred] = Proof.parse_body(block_lines, obj_map)
                            block_lines = []

                        # The end of the block.
                        if line_idx == len(lines):
                            break

                        # An Else-if row.
                        if (else_if_match := re.search(ELSE_IF_PATTERN, lines[line_idx])) is not None:
                            pred = parse_predicate(else_if_match.group(1), obj_map)
                            line_idx += 1
                            continue

                        # The end of the last block.
                        if not lines[line_idx][len(whitespace)].isspace():
                            break

                        # Just a line
                        block_lines.append(lines[line_idx])
                        line_idx += 1

                    steps.append(IfStep(pred_dict))
                else:
                    raise ProofParseError(f'Failed to parse proof: line {line} fits no pattern!')
        except Exception as e:
            raise ProofParseError(f'Error when parsing line {lines[line_idx - 1]} ====> Because of {e}') from e

        return steps

    @staticmethod
    def parse_embeds(data: list[str], obj_map: dict[str, GeoObject]) -> Embedding:
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

    @staticmethod
    def get_full_proof_path(path: Path) -> Path:
        full_path_options = [BASE_PATH / 'rules/proof_samples' / path, BASE_PATH / path, Path(path)]

        for path in full_path_options:
            if path.exists():
                return path
        else:
            raise Exception(f'Proof file {path} was not found.')

    @staticmethod
    def parse(data: str, parse_proof_body: bool = True) -> 'Proof':
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

        assumption_objects, assumption_preds = Proof.parse_assumptions(assumption_lines)
        target_objects, target_preds = Proof.parse_targets(target_lines, dict(assumption_objects))
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

        steps = Proof.parse_body(proof_lines, dict(assumption_objects)) if parse_proof_body else []

        embedding = Proof.parse_embeds(embed_lines, assumption_objects) if len(embed_lines) > 0 else None

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

    def to_language_format(self) -> str:
        """
        Converts the proof to a human readable format.
        @return: A string containing the proof.
        """
        assumptions = [ASSUMPTION_TITLE]
        embeds = [EMBED_TITLE]
        need_to_prove = [TARGET_TITLE]
        proof_body = [BODY_TITLE]

        # Representing the assumptions.
        objects_by_type = defaultdict(list)
        for obj in self.assumption_objects.values():
            if obj not in self.target_objects:
                objects_by_type[obj.type].append(obj)

        for type_, objects in objects_by_type.items():
            assumptions.append(', '.join(obj.name for obj in objects) + ': ' + type_)

        for known_pred in self.assumption_predicates:
            assumptions.append(known_pred.to_language_format())

        # Representing the embeds.
        if self.embedding is not None:
            for name, embedded_object in self.embedding.items():
                embeds.append(f'{name} := {json.dumps(embedded_object.to_dict())}')
        else:
            embeds = []

        # Representing the need-to-prove.
        objects_by_type = defaultdict(list)
        for obj in self.target_objects.values():
            objects_by_type[obj.type].append(obj)

        for type_, objects in objects_by_type.items():
            need_to_prove.append(', '.join(obj.name for obj in objects) + ': ' + type_)

        for pred in self.target_predicates:
            need_to_prove.append(pred.to_language_format())

        # Representing the steps.
        for step in self.steps:
            proof_body.append(step.to_language_format())

        assumptions_string = '\n'.join(assumptions)
        embeds_string = '\n'.join(embeds)
        need_to_prove_string = '\n'.join(need_to_prove)
        proof_body_string = '\n'.join(proof_body)

        proof_string = '\n\n'.join(
            filter(None, [assumptions_string, embeds_string, need_to_prove_string, proof_body_string])
        )

        return proof_string + '\n'

    def shuffled(self):
        """
        Shuffles the names of the objects in the proof.
        """
        out_names = set()

        def gen_name(obj: GeoObject) -> str:
            """
            Generates a name for an object.
            """
            type_prefix = obj.type[0].lower() + '_'
            l = 1
            attempts = 0
            while (
                new_name := type_prefix + ''.join(random.choice(string.ascii_uppercase) for _ in range(l))
            ) in out_names:
                attempts += 1
                if attempts == 5:
                    l += 1
                    attempts = 0

            out_names.add(new_name)
            return new_name

        # Due to possible conclusions, this is no longer allowed.
        # random.shuffle(self.assumptions)

        subs = {}
        for obj in itertools.chain(
            self.assumption_objects.values(),
            self.target_objects.values(),
            sum((step.result_objects for step in self.steps if isinstance(step, TheoremStep)), []),
            (step.left_hand for step in self.steps if isinstance(step, ObjDefineStep)),
        ):
            if (not isinstance(obj, ConstructionObject) or isinstance(obj, EquationObject)) and obj.type != LITERAL:
                new_obj = GeoObject(gen_name(obj), obj.type)
                subs[obj] = new_obj

        res_assumption_objects = {}
        res_target_objects = {}
        res_assumption_predicates = []
        res_auxiliary_predicates = []
        res_targets = []
        res_steps = []

        for obj in self.assumption_objects.values():
            res_obj = obj.substitute(subs)
            res_assumption_objects[res_obj.name] = res_obj

        for obj in self.target_objects.values():
            res_obj = obj.substitute(subs)
            res_target_objects[res_obj.name] = res_obj

        for assumption in self.assumption_predicates:
            res_assumption_predicates.append(assumption.substitute(subs))

        for auxiliary_predicate in self.auxiliary_predicates:
            res_auxiliary_predicates.append(auxiliary_predicate.substitute(subs))

        for target_predicate in self.target_predicates:
            res_targets.append(target_predicate.substitute(subs))

        for step in self.steps:
            res_steps.append(step.substitute(subs))

        res_embeds = None
        if self.embedding is not None:
            res_embeds = {}
            for name, embedded_object in self.embedding.items():
                new_name = [value for obj, value in subs.items() if obj.name == name][0]
                res_embeds[new_name] = embedded_object

        return Proof(
            res_assumption_objects | res_target_objects,
            res_assumption_objects,
            res_assumption_predicates,
            res_auxiliary_predicates,
            res_target_objects,
            res_targets,
            res_embeds,
            res_steps,
        )

    def shallow_copy(self) -> 'Proof':
        """
        Returns a shallow copy of the proof.
        This makes duplicates of the proof's structures,
        but copies the references to all underlying objects.
        """
        return Proof(
            dict(self.all_objects),
            dict(self.assumption_objects),
            list(self.assumption_predicates),
            list(self.auxiliary_predicates),
            dict(self.target_objects),
            list(self.target_predicates),
            self.embedding.shallow_copy() if self.embedding is not None else None,
            list(self.steps),
        )

    def strip_comments(self) -> 'Proof':
        """
        Removes all comments from the proof.
        """
        res = self.shallow_copy()
        for step in res.steps:
            if isinstance(step, TheoremStep):
                step.comment = ''
        return res

    def starting_predicates(self) -> list[Predicate]:
        return self.assumption_predicates + self.auxiliary_predicates


def test_pretty_print():
    from util import BASE_PATH

    path = BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G2.txt'
    proof = Proof.parse(path.open().read())
    print(proof.to_language_format())


def test_parse_if():
    from util import BASE_PATH

    path = BASE_PATH / 'rules/proof_samples/_test.txt'
    proof = Proof.parse(path.open().read())

    # print(proof.all_objects)
    # print(proof.assumptions)
    # print(proof.target_objects)
    # print(proof.target_predicates)
    # print(proof.steps)
    # for pred, proof in proof.steps[-1].data.items():
    #     print(pred)
    #     print(proof.steps)
    print(proof.to_language_format())


def test_shuffle():
    from util import BASE_PATH

    proof = Proof.parse((BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G3.jl').open().read())

    print(proof.shuffled().to_language_format())


def test_parse():
    from util import BASE_PATH

    proof = Proof.parse((BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G2_numeric.jl').open().read())
    print(proof.to_language_format())


if __name__ == '__main__':
    # test_pretty_print()
    # test_parse_if()
    # test_shuffle()
    test_parse()
