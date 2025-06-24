from re import Match

from .....steps.comment_step import CommentStep

from ..abstract_step_reader import AbstractStepReader


class CommentStepReader(AbstractStepReader[CommentStep]):
    pattern = r'Comment: \w*(.*)'

    def read(self, line: str, match: Match[str]) -> CommentStep:
        comment = match.group(1).strip()
        return CommentStep(comment)
