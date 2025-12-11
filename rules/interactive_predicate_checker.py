from .parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from .parsers.predicate_parser.predicate_parser import PredicateParser
from .proof_checker_utils import get_linear_eqn_factors

from .embeddings.undefined_embedding_error import UndefinedEmbeddingError
from .geometry_objects.geo_object import GeoObject
from .geometry_trackers.geometry_tracker import GeometryTracker
from .geometry_trackers.linear_algebra_tracker.linear_expression import LinearExpression
from .predicates.predicate import Predicate


class InteractivePredicateChecker:
    geometry_tracker: GeometryTracker
    
    predicate_parser: PredicateParser
    geometry_object_parser: GeometryObjectParser

    def __init__(self, geometry_tracker: GeometryTracker):
        self.geometry_tracker = geometry_tracker

    def run(self):
        self.predicate_parser = PredicateParser(self.geometry_tracker.signature)
        self.geometry_object_parser = GeometryObjectParser(self.geometry_tracker.signature)

        while True:
            try:
                text = input('>> ')
                if text == 'quit()':
                    break

                if text.lower().startswith('!'):
                    text = text[1:]
                    obj = self.parse_geometry_object_or_predicate(text)
                    print(self.geometry_tracker.equality_tracker.normalize(obj))
                elif text.lower().startswith('?'):
                    text = text[1:]
                    predicate = self.predicate_parser.try_parse(text)
                    if predicate is None:
                        raise ValueError("Could not parase predicate")
                    factors = get_linear_eqn_factors(predicate)
                    if factors is None:
                        raise ValueError("Invalid factors")
                    if self.geometry_tracker.embedding_tracker is None:
                        raise ValueError("Cannot explain predicates without an embedding.")
                    if not self.geometry_tracker.contains_predicate(predicate, can_add=False):
                        raise ValueError("Predicate is False.")
                    explanation = self.geometry_tracker._linear_algebra.explain_relation(LinearExpression(factors))
                    print('\n'.join([str(p) for p in explanation]))
                else:
                    obj = self.parse_geometry_object_or_predicate(text)
                    if isinstance(obj, GeoObject):
                        self.print_geometry_object(obj)
                    else:
                        print(self.check_predicate(obj))
            except KeyboardInterrupt:
                print()
            except Exception as e:
                print(e)

    def check_predicate(self, predicate: Predicate) -> str:
        is_predicate_proved = self.geometry_tracker.contains_predicate(predicate, can_add=False)
        if self.geometry_tracker.embedding_tracker is None:
            return f'{is_predicate_proved}'

        is_predicate_true_in_embedding = self.geometry_tracker.embedding_tracker.evaluate_predicate(predicate)
        return f'{is_predicate_proved} ({is_predicate_true_in_embedding.value} in embedding)'

    def print_geometry_object(self, obj: GeoObject):
        if self.geometry_tracker.embedding_tracker is None:
            print('Failed to evaluate.')
        else:
            try:
                result = self.geometry_tracker.embedding_tracker.evaluate_object(obj)
                if len(result) == 0:
                    raise UndefinedEmbeddingError()
                elif len(result) == 1:
                    print(result[0].to_str(4))
                else:
                    prefix_length = len(str(len(result) + 1))
                    for i, embedded_obj in enumerate(result):
                        print(f'{i + 1:>{prefix_length}}: {embedded_obj.to_str(4)}')
            except UndefinedEmbeddingError:
                print('Failed to evaluate in embedding.')
                
    def parse_geometry_object_or_predicate(self, text: str) -> GeoObject | Predicate:
        geo_object = self.geometry_object_parser.try_parse(text)
        if geo_object is not None:
            return geo_object
        predicate = self.predicate_parser.try_parse(text)
        if predicate is not None:
            return predicate
        raise ValueError("Input could not be parsed as either a Predicate or a GeoObject")
