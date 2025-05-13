from re import Match

from ......geometry_objects.geo_object import GeoObject

from .....steps.comment_step import CommentStep

from ..abstract_step_reader import AbstractStepReader


class CommentStepReader(AbstractStepReader[CommentStep]):
    pattern = r'Comment: \w*(.*)'

    def read(line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> CommentStep:
        comment = match.group(1).strip()
        return CommentStep(comment)
