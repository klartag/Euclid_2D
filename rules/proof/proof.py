from .steps import Step, TheoremStep


class Proof:
    """
    A class representing a proof.
    """

    steps: list[Step]

    def __init__(
        self,
        steps: list[Step],
    ):
        self.steps = steps

    def shallow_copy(self) -> 'Proof':
        """
        Returns a shallow copy of the proof.
        This makes duplicates of the proof's structures,
        but copies the references to all underlying objects.
        """
        return Proof(self.steps[:])

    def strip_comments(self) -> 'Proof':
        """
        Removes all comments from the proof.
        """
        res = self.shallow_copy()
        for step in res.steps:
            if isinstance(step, TheoremStep):
                step.comment = ''
        return res
