from re import Match

from ......expression_parse_utils import split_args
from ......errors import ProofParseError
from ......geometry_objects.atom import Atom
from ......geometry_objects.geo_object import GeoObject
from ......geometry_objects.parse import parse_geo_object
from ......predicates.predicate_factory import parse_predicate
from ......theorem import Theorem

from .....steps.theorem_step import TheoremStep

from ..abstract_step_reader import AbstractStepReader


class TheoremStepReader(AbstractStepReader[TheoremStep]):
    pattern = r'By (\w+)( on )?(.*) we get (.*)$'

    def read(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> TheoremStep:
        # Matching a theorem step using a named theorem.
        name, _, args, results = match.groups()
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
            res = Atom(cons_name, typ)
            obj_map[cons_name] = res
            result_objects.append(res)

        result_predicates = [parse_predicate(result, obj_map) for result in results[len(theorem.result_objects) :]]
        return TheoremStep(name, inputs, result_objects, result_predicates, '')
