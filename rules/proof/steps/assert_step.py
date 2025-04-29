@dataclass
class AssertStep(Step):
    """
    A step of the form:
    We have shown that A, B, C.
    """

    predicates: list[Predicate]

    def to_language_format(self) -> str:
        return f'We have shown ' + ', '.join(pred.to_language_format() for pred in self.predicates)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return AssertStep([pred.substitute(subs) for pred in self.predicates])
