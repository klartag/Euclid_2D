import functools
import itertools
from pathlib import Path

from rules.parsers.predicate_parser.predicate_parser import PredicateParser
from util import BASE_PATH

from .rule_utils import unpack_dict
from .errors import ProofParseError
from .geometry_objects.geo_type import GeoType, Signature
from .geometry_objects.atom import Atom
from .geometry_objects.geo_object import GeoObject
from .predicates.predicate import Predicate
from .predicates.predicate_factory import predicate_from_args

THEOREM_FOLDER = BASE_PATH / 'rules' / 'theorems'


INPUT_LABEL = 'inputs'
CONDITION_LABEL = 'where'
EMBEDDING_CONDITION_LABEL = 'where_embedding'
CONSTRUCTION_LABEL = 'construct'
RESULT_PREDICATE_LABEL = 'conclude'
POSS_CONCLUSIONS_LABEL = 'possible_conclusions'
TRIVIAL_IF_EQUAL_LABEL = 'trivial_if_equal'
RANK = 'rank'
METADATA_LABEL = 'metadata'


class Theorem:
    name: str
    data: str
    signature: list[GeoObject]
    """The required types of objects."""
    required_predicates: list[Predicate]
    """The predicates the objects should satisfy."""
    required_embedding_predicates: list[Predicate]
    """The predicates the objects should satisfy."""
    result_objects: list[GeoObject]
    """The objects constructed by the theorem."""
    result_predicates: list[Predicate]
    """The predicates constructed by the theorem."""
    trivial_if_equal_conditions: list[list[list[str]]]
    """Groups of object names such that if they are equal,
    the entire Theorem is too trivial for the Proof Generator to apply"""
    rank: int
    """How interesting it is to apply the theorem.
    (See the `" rank` title under the `theorems_design.md` file for more info)"""
    metadata: str
    path: Path = None
    """Path of the file where the theorem is stored."""

    def __init__(
        self,
        name: str,
        data: str,
        signature: list[GeoObject],
        required_predicates: list[Predicate],
        required_embedding_predicates: list[Predicate],
        result_objects: list[GeoObject],
        result_predicates: list[Predicate],
        trivial_if_equal_conditions: list[list[list[str]]],
        rank: int,
        metadata: str,
        path: Path = None,
    ):
        self.name = name
        self.data = data
        self.signature = signature
        self.required_predicates = required_predicates
        self.required_embedding_predicates = required_embedding_predicates
        self.result_objects = result_objects
        self.result_predicates = result_predicates
        self.trivial_if_equal_conditions = trivial_if_equal_conditions
        self.rank = rank
        self.metadata = metadata
        self.path = path

    def __repr__(self):
        return f'Theorem({self.name})'

    @staticmethod
    def read(path: Path) -> 'list[Theorem]':
        assert (
            path.suffix == '.yml' or path.suffix == '.yaml'
        ), f'Theorems must be stored in YAML files! Tried to open {path}'

        import re
        from ruamel.yaml import YAML

        theorem_data = YAML(typ='safe', pure=True).load(path)
        return Theorem.parse_dict(theorem_data, path)

    @staticmethod
    def parse_dict(theorem_data: dict, path: Path = None) -> 'list[Theorem]':
        """
        Reads the theorem from the given theorem file.
        """
        res: list[Theorem] = []
        for theorem_name, data in theorem_data.items():
            try:
                signature: list[GeoObject] = []
                type_signature: Signature = {}
                required_predicates: list[Predicate] = []
                required_embedding_predicates: list[Predicate] = []
                result_objects: list[GeoObject] = []
                result_predicates: list[Predicate] = []
                conclusion_flows: dict[str, str] = {}
                trivial_if_equal_conditions = []
                predicate_map = {}

                # Parsing.
                for names, type_ in map(unpack_dict, data.get(INPUT_LABEL, [])):
                    for name in names.split(','):
                        name = name.strip()
                        assert name not in signature, f'In theorem {theorem_name}, object name {name} appears twice!'
                        g = Atom(name, GeoType(type_))
                        type_signature[name] = GeoType(type_)
                        signature.append(g)

                signature_objects = tuple(x for x in signature if x.type not in [GeoType.SCALAR, GeoType.ANGLE])
                required_predicates.append(predicate_from_args('exists', signature_objects))

                # The construction part is the third part, and not the second. We parse it second to get the result object definitions.
                for names, type_ in map(unpack_dict, data.get(CONSTRUCTION_LABEL, [])):
                    for name in names.split(','):
                        name = name.strip()
                        assert name not in signature, f'In theorem {theorem_name}, object name {name} appears twice!'
                        g = Atom(name, GeoType(type_))
                        type_signature[name] = GeoType(type_)
                        result_objects.append(g)

                predicate_parser = PredicateParser(type_signature)

                for predicate_block in data.get(CONDITION_LABEL, []):
                    match predicate_block:
                        # Named predicates
                        case dict():
                            name, predicate_data = unpack_dict(predicate_block)
                            predicate = predicate_parser.try_parse(predicate_data)
                            predicate_map[name] = predicate
                        case str():
                            predicate = predicate_parser.try_parse(predicate_block)
                            required_predicates.append(predicate)
                        case _:
                            raise NotImplementedError(
                                f'Unknown predicate block type {type(predicate_block)} in theorem {theorem_name}'
                            )

                for predicate_block in data.get(EMBEDDING_CONDITION_LABEL, []):
                    match predicate_block:
                        # Named predicates
                        case str():
                            predicate = predicate_parser.try_parse(predicate_block)
                            required_embedding_predicates.append(predicate)
                        case _:
                            raise NotImplementedError(
                                f'Unknown predicate block type {type(predicate_block)} in theorem {theorem_name}'
                            )

                for predicate_block in data.get(RESULT_PREDICATE_LABEL, []):
                    match predicate_block:
                        # Unnamed predicates
                        case dict():
                            name, predicate_data = unpack_dict(predicate_block)
                            predicate = predicate_parser.try_parse(predicate_data)
                            predicate_map[name] = predicate
                        case str():
                            assert (
                                '=>' not in predicate_block
                            ), f'=> is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                            assert (
                                '<=' not in predicate_block
                            ), f'<= is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                            predicate = predicate_parser.try_parse(predicate_block)
                            result_predicates.append(predicate)
                        case _:
                            raise NotImplementedError(
                                f'Unknown predicate block type {type(predicate_block)} in theorem {theorem_name}'
                            )

                for conclusion_flow in data.get(POSS_CONCLUSIONS_LABEL, []):
                    match conclusion_flow:
                        # Named conclusions
                        case dict():
                            assert len(conclusion_flow) == 1
                            name, conclusion = unpack_dict(conclusion_flow)
                            conclusion_flows[name] = conclusion
                        # Unnamed conclusions
                        case str():
                            i = 0
                            while f'{theorem_name}_v{i}' in conclusion_flows:
                                i += 1
                            conclusion_flows[f'{theorem_name}_v{i}'] = conclusion_flow

                trivial_if_equal_conditions = data.get(TRIVIAL_IF_EQUAL_LABEL, [])

                rank: int = data.get(RANK, 0)

                for i in range(len(trivial_if_equal_conditions)):
                    if isinstance(trivial_if_equal_conditions[i][0], str):
                        trivial_if_equal_conditions[i] = [[obj_name] for obj_name in trivial_if_equal_conditions[i]]

                # Validating the predicates.
                for pred in itertools.chain(
                    required_predicates + required_embedding_predicates, result_predicates, predicate_map.values()
                ):
                    if not pred.is_valid():
                        raise ValueError(f'In theorem {theorem_name}, predicate {pred} is invalid!')

                metadata = data.get(METADATA_LABEL, '')

                # Building the base theorem, without any conclusion flows.
                # We build it only if there are results not using the conclusion flows.
                if len(result_predicates) > 0 or len(result_objects) > 0:
                    res.append(
                        Theorem(
                            theorem_name,
                            data,
                            signature,
                            required_predicates,
                            required_embedding_predicates,
                            result_objects,
                            result_predicates,
                            trivial_if_equal_conditions,
                            rank,
                            metadata,
                            path,
                        )
                    )

                for flow_name, flow in conclusion_flows.items():
                    # Splitting the conclusion flow
                    if '<=>' in flow:
                        left, right = flow.split('<=>')
                        symbol = '<=>'
                    elif '<=' in flow:
                        left, right = flow.split('<=')
                        symbol = '<='
                    elif '=>' in flow:
                        left, right = flow.split('=>')
                        symbol = '=>'
                    else:
                        raise ProofParseError(f'Conclusion flow symbol not found in line {flow}!')

                    left_parts = [part.strip() for part in left.split('&')]
                    left_preds = [
                        predicate_map[part] if part in predicate_map else predicate_parser.try_parse(part)
                        for part in left_parts
                    ]

                    right_parts = [part.strip() for part in right.split('&')]
                    right_preds = [
                        predicate_map[part] if part in predicate_map else predicate_parser.try_parse(part)
                        for part in right_parts
                    ]

                    assert symbol in ['<=', '=>', '<=>']

                    if symbol[0] == '<':
                        rev_name = f'{flow_name}_r' if symbol[-1] == '>' else flow_name
                        res.append(
                            Theorem(
                                rev_name,
                                data,
                                signature,
                                required_predicates + right_preds,
                                required_embedding_predicates,
                                result_objects,
                                result_predicates + left_preds,
                                trivial_if_equal_conditions,
                                rank,
                                metadata,
                                path,
                            )
                        )
                    if symbol[-1] == '>':
                        res.append(
                            Theorem(
                                flow_name,
                                data,
                                signature,
                                required_predicates + left_preds,
                                required_embedding_predicates,
                                result_objects,
                                result_predicates + right_preds,
                                trivial_if_equal_conditions,
                                rank,
                                metadata,
                                path,
                            )
                        )
            except Exception as e:
                e.args = (f'In theorem {theorem_name}:\n{e.args[0]}',) + e.args[1:]
                raise e

        return res

    @functools.cache
    @staticmethod
    def all_theorems() -> 'dict[str, Theorem]':
        """
        Parses all theorems in the theorem folder.
        """
        res = {}
        filenames = {}

        for addr in THEOREM_FOLDER.rglob('*.yml'):
            theorems = Theorem.read(addr)
            for theorem in theorems:
                if theorem.name in filenames:
                    raise ProofParseError(
                        f'Theorem {theorem.name} defined both in {addr} and in {filenames[theorem.name]}!'
                    )
                filenames[theorem.name] = addr
                res[theorem.name] = theorem

        return res

    @staticmethod
    def from_name(name: str) -> 'Theorem | None':
        """
        Returns the theorem with the given name from the theorems directory.
        @param name: The name of the theorem.
        """
        return Theorem.all_theorems().get(name, None)


all_theorems = Theorem.all_theorems
from_name = Theorem.from_name

if __name__ == '__main__':
    from util import BASE_PATH

    for theorem in all_theorems().values():
        print(theorem.name)
