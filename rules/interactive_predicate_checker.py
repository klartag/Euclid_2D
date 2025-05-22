from .parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from .parsers.predicate_parser.predicate_parser import PredicateParser

from .embeddings.undefined_embedding_error import UndefinedEmbeddingError
from .geometry_objects.atom import Atom
from .geometry_objects.geo_object import GeoObject
from .geometry_trackers.geometry_tracker import GeometryTracker
from .predicates.predicate import Predicate


class InteractivePredicateChecker:
    geometry_tracker: GeometryTracker

    def __init__(self, geometry_tracker: GeometryTracker):
        self.geometry_tracker = geometry_tracker

    def run(self):
        signature = {atom.name: atom.type for atom in self.geometry_tracker.all_objects() if isinstance(atom, Atom)}

        predicate_parser = PredicateParser(signature)
        geometry_object_parser = GeometryObjectParser(signature)

        while True:
            try:
                text = input('>> ')
                if text == 'quit()':
                    break
                try:
                    predicate = predicate_parser.try_parse(text)
                    if predicate is None:
                        raise ValueError("User input was not a predicate.")
                    print(self.check_predicate(predicate))
                except Exception as e0:
                    try:
                        geo_object = geometry_object_parser.try_parse(text)
                        self.print_geometry_object(geo_object)
                    except Exception as e1:
                        print(
                            f'Failed to evaluate as either geometry object or predicate due to the following exceptions:'
                        )
                        print(e0)
                        if str(e0) != str(e1):
                            print(e1)
            except KeyboardInterrupt:
                print()

    def check_predicate(self, predicate: Predicate) -> str:
        is_predicate_proved = self.geometry_tracker.contains_predicate(predicate)
        if self.geometry_tracker.embedding_tracker is None:
            return f'{is_predicate_proved}'

        is_predicate_true_in_embedding = self.geometry_tracker.embedding_tracker.evaluate_predicate(predicate)
        return f'{is_predicate_proved} ({is_predicate_true_in_embedding.value} in embedding)'

    def print_geometry_object(self, obj: GeoObject) -> str:
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
