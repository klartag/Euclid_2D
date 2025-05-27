from re import Match


from ......expression_parse_utils import split_args
from ......errors import ProofParseError
from ......parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from ......parsers.predicate_parser.predicate_parser import PredicateParser

from ......theorem import Theorem
from ......geometry_objects.geo_type import Signature

from .....steps.theorem_step import TheoremStep

from ..abstract_step_reader import AbstractStepReader


class TheoremStepReader(AbstractStepReader[TheoremStep]):
    pattern = r'By (\w+)( on )?(.*) we get (.*)$'

    geometry_object_parser: GeometryObjectParser
    predicate_parser: PredicateParser

    def __init__(self, signature: Signature):
        self.geometry_object_parser = GeometryObjectParser(signature)
        self.predicate_parser = PredicateParser(signature)

    def read(self, line: str, match: Match[str]) -> TheoremStep:
        # Matching a theorem step using a named theorem.
        name, _, args, results = match.groups()
        args = split_args(args) if args else []
        results = split_args(results)

        if name not in Theorem.all_theorems():
            raise ProofParseError(f'Proof used unknown theorem: {name} in line {line}!')
        theorem = Theorem.all_theorems().get(name, None)
        if theorem is None:
            raise ProofParseError(f'In line {line}, theorem {name} is unknown!')

        inputs = [self.geometry_object_parser.try_parse(arg.strip()) for arg in args]
        if len(inputs) > len(theorem.signature):
            raise ProofParseError(f'In line {line}, too many arguments for theorem {name}!')
        if len(inputs) < len(theorem.signature):
            raise ProofParseError(f'In line {line}, too few arguments for theorem {name}!')

        result_predicates = [self.predicate_parser.try_parse(result) for result in results]
        return TheoremStep(name, inputs, result_predicates, '')
