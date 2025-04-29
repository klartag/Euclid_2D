@dataclass
class ObjDefineStep(Step):
    """
    A step that defines a new object. Can be used either as:
    Let a := tangent(B, c)
    Or as:
    We introduce tangent(B, c)
    """

    left_hand: GeoObject
    right_hand: GeoObject | None = dataclasses.field(default=None)

    def to_language_format(self) -> str:
        if self.right_hand is not None:
            return f'Let {self.left_hand.name} := {self.right_hand.name}'
        else:
            return f'We introduce {self.left_hand.name}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return ObjDefineStep(
            self.left_hand.substitute(subs), self.right_hand.substitute(subs) if self.right_hand is not None else None
        )
