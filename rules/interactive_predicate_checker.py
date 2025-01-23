from rules.geometry_trackers.geometry_tracker import GeometryTracker
from rules.predicates.predicate_factory import parse_predicate


class InteractivePredicateChecker:
    geometry_tracker: GeometryTracker

    def __init__(self, geometry_tracker: GeometryTracker):
        self.geometry_tracker = geometry_tracker

    def run(self):
        object_map = {o.name: o for o in self.geometry_tracker.all_objects() if o.name.isalnum()}
        while True:
            try:
                predicate_data = input('>> ')
                if predicate_data == 'quit()':
                    break
                predicate = parse_predicate(predicate_data, object_map)
                print(self.geometry_tracker.contains_predicate(predicate))
            except Exception as e0:
                print(f'Raised exception: {e0}')
            except KeyboardInterrupt:
                print()
