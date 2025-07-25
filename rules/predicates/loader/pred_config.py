import itertools
from pathlib import Path

from util import BASE_PATH

from ...rule_utils import unpack_dict
from ...parsers.predicate_parser.predicate_parser import PredicateParser
from ...theorem import CONDITION_LABEL, CONSTRUCTION_LABEL, POSS_CONCLUSIONS_LABEL, RESULT_PREDICATE_LABEL
from ...errors import ProofParseError
from ...symmetry import Symmetry

from ...geometry_objects.atom import Atom
from ...geometry_objects.construction_object import Construction, LogConstruction
from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.geo_type import GeoType, Signature

from .. import global_predicates

from ..predicate import INPUT_LABEL, PREPROCESS_LABEL, Predicate
from ..implementations.macro_predicate import MacroData


MACRO_FOLDER = BASE_PATH / 'rules' / 'constructions_and_predicates' / 'hierarchy' / 'predicates'
CONSTRUCTION_FOLDER = BASE_PATH / 'rules' / 'constructions_and_predicates' / 'hierarchy' / 'constructions'


def file_priority(path: Path) -> str:
    """
    Picks a priority by which the files are loaded.
    """
    filename = path.stem
    if '_' in filename:
        parts = filename.split('_')
        parts = parts[-1:] + parts[:-1]
        return '_'.join(parts)
    return f'0_{filename}'


def load_constructions_and_macros() -> None:
    """
    Loads the constructions and the macros.
    """

    log_arg_0 = Atom('arg_0', GeoType.SCALAR)
    global_constructions: dict[str, Construction] = {
        'log': LogConstruction(
            'log',
            [log_arg_0],
            Symmetry.NONE,
            Atom('res', GeoType.SCALAR),
            [],
            [],
        ),
    }
    global_macros: dict[str, MacroData] = {}

    global_predicates._CONSTRUCTIONS = global_constructions
    global_predicates._MACROS = global_macros

    construction_paths = CONSTRUCTION_FOLDER.glob('*.yml')
    predicate_paths = MACRO_FOLDER.glob('*.yml')

    all_paths = [(path, False) for path in construction_paths] + [(path, True) for path in predicate_paths]
    all_paths = sorted(all_paths, key=lambda t: (file_priority(t[0]), t[1]))

    # Storing the file in which we have found each object.
    macro_filenames = {}
    construction_filenames = {}
    for filename, is_pred_file in all_paths:
        if is_pred_file:
            macros = read_macros(filename)
            for macro in macros:
                if macro.name in macro_filenames:
                    raise ProofParseError(
                        f'Macto {macro.name} defined both in {filename} and in {macro_filenames[macro.name]}!'
                    )
                macro_filenames[macro.name] = filename
                global_macros[macro.name] = macro
        else:
            constructions = read_constructions(filename)
            for construction in constructions:
                if construction.name in construction_filenames:
                    raise ProofParseError(
                        f'Construction {construction.name} defined both in {filename} and in {construction_filenames[construction.name]}!'
                    )
                construction_filenames[construction.name] = filename
                global_constructions[construction.name] = construction


def read_constructions(path: Path) -> list[Construction]:
    """
    Reads the theorem from the given theorem file.
    """
    assert (
        path.suffix == '.yml' or path.suffix == '.yaml'
    ), f'Constructions must be stored in YAML files! Tried to open {path}'

    from ruamel.yaml import YAML

    construction_data = YAML(typ='safe', pure=True).load(path)

    all_constructions: list[Construction] = []

    for construction_name, data in construction_data.items():
        objects: list[GeoObject] = []
        signature: Signature = {}
        required_predicates: list[Predicate] = []
        result_predicates: list[Predicate] = []

        # 1. Parsing the inputs.
        for names, type_ in map(unpack_dict, data.get(INPUT_LABEL, [])):
            for name in names.split(','):
                name = name.strip()
                assert name not in signature, f'In theorem {construction_name}, object name {name} appears twice!'
                g = Atom(name, GeoType(type_))
                signature[name] = GeoType(type_)
                objects.append(g)

        predicate_parser = PredicateParser(signature)

        # 2. Parsing the preprocess type.
        preprocess = Symmetry.parse(data.get(PREPROCESS_LABEL, 'none'))

        # 3. Parsing the conditions.
        for pred in data.get(CONDITION_LABEL, []):
            parsed_pred: Predicate = predicate_parser.try_parse(pred)
            required_predicates.append(parsed_pred)

        # 4. Parsing the constructed object.
        res = data.get(CONSTRUCTION_LABEL, [])
        if len(res) != 1:
            raise ProofParseError(f'Illegal construction result in construction {construction_name}: {res}')
        if isinstance(res, list):
            res = res[0]
            if len(res) != 1:
                raise ProofParseError(f'Illegal construction result in construction {construction_name}: {res}')
        if not isinstance(res, dict):
            raise ProofParseError(f'Unrecognized result object in construction {construction_name}: {res}')

        res_name, res_typ = unpack_dict(res)
        assert res_name not in signature, f'In construction {construction_name}, object name {res_name} appears twice!'
        res_obj = Atom(res_name, GeoType(res_typ))
        signature[res_name] = GeoType(res_typ)

        # Updating the Predicate Parser to work with the updated signature
        predicate_parser = PredicateParser(signature)

        # 5. Parsing the result predicate.
        predicate_map = {}
        for predicate_block in data.get(RESULT_PREDICATE_LABEL, []):
            match predicate_block:
                # Unnamed predicates
                case dict():
                    name, predicate_data = unpack_dict(predicate_block)
                    pred = predicate_parser.try_parse(predicate_data)
                    predicate_map[name] = pred
                case str():
                    assert (
                        '=>' not in predicate_block
                    ), f'=> is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                    assert (
                        '<=' not in predicate_block
                    ), f'<= is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                    pred = predicate_parser.try_parse(predicate_block)
                    result_predicates.append(pred)
                case _:
                    raise NotImplementedError(
                        f'Unknown predicate block type {type(predicate_block)} in construction {construction_name}'
                    )

        # 6. Parsing the possible conclusions.
        possible_conclusions = []
        for flow in data.get(POSS_CONCLUSIONS_LABEL, []):
            if '<=>' in flow:
                left, right = flow.split('<=>')
                symbol = '<=>'
            elif '<=' in flow:
                right, left = flow.split('<=')
                symbol = '=>'
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

            match symbol:
                case '=>':
                    possible_conclusions.append((left_preds, right_preds))
                case '<=>':
                    possible_conclusions.append((right_preds, left_preds))
                    possible_conclusions.append((left_preds, right_preds))
                case _:
                    raise ProofParseError(f'Conclusion flow symbol {symbol} should not exist!')

        # Validating the predicates.
        for pred in itertools.chain(required_predicates, result_predicates, predicate_map.values()):
            if not pred.is_valid():
                raise ValueError(f'In construction {construction_name}, predicate {pred} is invalid!')

        all_constructions.append(
            Construction(
                construction_name,
                objects,
                preprocess,
                res_obj,
                required_predicates,
                result_predicates,
                possible_conclusions,
            )
        )

    return all_constructions


def read_macros(path: Path) -> 'list[MacroData]':
    """
    Reads the macros from the given path.
    """
    assert (
        path.suffix == '.yml' or path.suffix == '.yaml'
    ), f'Constructions must be stored in YAML files! Tried to open {path}'

    from ruamel.yaml import YAML

    macro_data = YAML(typ='safe', pure=True).load(path)

    all_macros: list[MacroData] = []

    for macro_name, data in macro_data.items():
        try:
            objects: list[GeoObject] = []
            signature: Signature = {}
            unpack_predicates: list[Predicate] = []
            conclude_self = False
            # 1. Parsing the inputs.
            for names, type_ in map(unpack_dict, data.get(INPUT_LABEL, [])):
                for name in names.split(','):
                    name = name.strip()
                    assert name not in signature, f'In macro {macro_name}, object name {name} appears twice!'
                    g = Atom(name, GeoType(type_))
                    objects.append(g)
                    signature[name] = GeoType(type_)

            predicate_parser = PredicateParser(signature)

            # 2. Parsing the preprocess type.
            preprocess = Symmetry.parse(data.get(PREPROCESS_LABEL, 'none'))
            # 3. Parsing the result predicates.
            predicate_map = {}
            for predicate_block in data.get(RESULT_PREDICATE_LABEL, []) or []:
                match predicate_block:
                    # Unnamed predicates
                    case dict():
                        name, predicate_data = unpack_dict(predicate_block)
                        pred = predicate_parser.try_parse(predicate_data)
                        predicate_map[name] = pred
                    case str():
                        assert (
                            '=>' not in predicate_block
                        ), f'=> is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                        assert (
                            '<=' not in predicate_block
                        ), f'<= is not allowed in a conclusion statement. Did you mean to use it in a {POSS_CONCLUSIONS_LABEL} block?'
                        if predicate_block == 'self':
                            conclude_self = True
                        else:
                            pred = predicate_parser.try_parse(predicate_block)
                            unpack_predicates.append(pred)
                    case _:
                        raise ProofParseError(
                            f'Unknown predicate block type {type(predicate_block)} in macro {macro_name}'
                        )

            # 4. Parsing the possible conclusions.
            possible_conclusions = []
            for flow in data.get(POSS_CONCLUSIONS_LABEL, []):
                if '<=>' in flow:
                    left, right = flow.split('<=>')
                    symbol = '<=>'
                elif '<=' in flow:
                    right, left = flow.split('<=')
                    symbol = '=>'
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

                match symbol:
                    case '=>':
                        possible_conclusions.append((left_preds, right_preds))
                    case '<=>':
                        possible_conclusions.append((right_preds, left_preds))
                        possible_conclusions.append((left_preds, right_preds))
                    case _:
                        raise ProofParseError(f'Conclusion flow symbol {symbol} should not exist!')

            # Validating the predicates.
            for pred in unpack_predicates:
                if not pred.is_valid():
                    raise ValueError(f'In macro {macro_name}, predicate {pred} is invalid!')

            all_macros.append(
                MacroData(
                    macro_name,
                    preprocess,
                    objects,
                    unpack_predicates,
                    possible_conclusions,
                    conclude_self,
                )
            )

        except Exception as e:
            raise ProofParseError(f'When parsing {macro_name}: we get {e}') from e

    return all_macros
