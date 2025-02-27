from .geometry_objects.geo_object import GeoObject
from .geometry_objects.parse import parse_geo_object
from .geometry_trackers.geometry_tracker import GeometryTracker

from .predicates.predicate import Predicate
from .predicates.predicate_factory import parse_predicate


class InteractivePredicateChecker:
    geometry_tracker: GeometryTracker

    def __init__(self, geometry_tracker: GeometryTracker):
        self.geometry_tracker = geometry_tracker

    def run(self):
        object_map = {o.name: o for o in self.geometry_tracker.all_objects() if o.name.isalnum()}
        while True:
            try:
                data = input('>> ')
                if data == 'quit()':
                    break
                try:
                    predicate = parse_predicate(data, object_map)
                    print(self.check_predicate(predicate))
                except Exception as e0:
                    try:
                        geo_object = parse_geo_object(data, object_map)
                        print(self.check_geometry_object(geo_object))
                    except Exception as e1:
                        print(f'Failed to evaluate as either construction or predicate due to the following exceptions:')
                        print(e0)
                        if str(e0) != str(e1):
                            print(e1)
            except KeyboardInterrupt:
                print()
    
    def check_predicate(self, predicate: Predicate) -> str:
        is_predicate_proved = self.geometry_tracker.contains_predicate(predicate)
        is_predicate_true_in_embedding = self.geometry_tracker.embedding_tracker.evaluate_predicate(predicate)
        return f'{is_predicate_proved} ({is_predicate_true_in_embedding.value} in embedding)'

    def check_geometry_object(self, obj: GeoObject) -> str:
        embedded_object = self.geometry_tracker.embedding_tracker.evaluate_object(obj)
        if embedded_object is None:
            return 'Failed to evaluate in embedding.'
        else:
            return 'Successfully evaluated in embedding.'
