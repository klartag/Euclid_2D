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

    def __init__(self, geometry_tracker: GeometryTracker):
        self.geometry_tracker = geometry_tracker

    def run(self):
        predicate_parser = PredicateParser(self.geometry_tracker.signature)
        geometry_object_parser = GeometryObjectParser(self.geometry_tracker.signature)

        while True:
            try:
                text = input('>> ')
                if text == 'quit()':
                    break

                if text.endswith('?'):
                    try:
                        predicate = predicate_parser.try_parse(text[:-1])
                        if predicate is None:
                            raise ValueError("User input was not a predicate.")
                        factors = get_linear_eqn_factors(predicate)
                        if factors is None:
                            raise ValueError("Invalid factors")
                        if self.geometry_tracker.embedding_tracker is None:
                            raise ValueError("Cannot explain predicates without an embedding.")
                        if not self.geometry_tracker.contains_predicate(predicate, can_add=False):
                            raise ValueError("Predicate is False.")
                        explanation = self.geometry_tracker._linear_algebra.explain_relation(LinearExpression(factors))
                        print('\n'.join([str(p) for p in explanation]))
                        continue
                    except:
                        pass

                try:
                    predicate = predicate_parser.try_parse(text)
                    if predicate is None:
                        raise ValueError("User input was not a predicate.")
                    print(self.check_predicate(predicate))
                    continue
                except:
                    pass
                
                try:
                    geo_object = geometry_object_parser.try_parse(text)
                    if geo_object is None:
                        raise ValueError("User input was not a geometry object.")
                    self.print_geometry_object(geo_object)
                    continue
                except:
                    pass
                
                print("An error occured.")
            except KeyboardInterrupt:
                print()

    def check_predicate(self, predicate: Predicate) -> str:
        is_predicate_proved = self.geometry_tracker.contains_predicate(predicate, can_add=False)
        if self.geometry_tracker.embedding_tracker is None:
            return f'{is_predicate_proved}'

        is_predicate_true_in_embedding = self.geometry_tracker.embedding_tracker.evaluate_predicate(predicate)
        return f'{is_predicate_proved} ({is_predicate_true_in_embedding.value} in embedding)'
    
    def explain_predicate(self, predicate: Predicate) -> str:
        raise NotImplementedError()

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
                    for i, obj in enumerate(result):
                        print(f'{i + 1:>{prefix_length}}: {obj.to_str(4)}')
            except UndefinedEmbeddingError:
                print('Failed to evaluate in embedding.')
