from re import Match

from ......rule_utils import split_args
from ......errors import ProofParseError
from ......geometry_objects.geo_type import GeoType
from ......geometry_objects.geo_object import GeoObject
from ......geometry_objects.atom import Atom
from ......predicates.predicate_factory import parse_predicate

from .....steps.null_theorem_step import NullTheoremStep

from ..abstract_step_reader import AbstractStepReader


class NullTheoremStepReader(AbstractStepReader[NullTheoremStep]):
    pattern = r'We have (.*)$'

    def read(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> NullTheoremStep:
        # Matching a theorem step without a defined theorem.
        results = match.group(1)
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
            res_obj = Atom(name, GeoType(typ))
            result_objects.append(res_obj)
            obj_map[name] = res_obj

        result_predicates = [parse_predicate(result, obj_map) for result in results]

        return NullTheoremStep(result_objects, result_predicates)
