from pathlib import Path
import time
from tqdm import tqdm

from ..embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPredicateCollector
from ..proof.document.document_section import DocumentSection
from ..proof.document.geometry_document import GeometryDocument
from ..proof.document.reader.document_reader import DocumentReader
from ..proof.document.writer.document_writer import DocumentWriter
from ..proof.geometry_problem import GeometryProblem
from ..proof.steps import CommentStep
from ..proof_checker import ProofChecker
from ..errors import ProofCheckError

MIN_CHECKPOINT_STEPS = 2


class ProofTrimmer:
    """
    TODO: Document
    """

    problem: GeometryProblem
    trimmed_problem: GeometryProblem
    checkpoints: list[ProofChecker]

    def __init__(self, problem: GeometryProblem):
        self.problem = problem
        self.trimmed_problem = self.problem.shallow_copy()
        self.checkpoints = []

    def trim(self) -> GeometryProblem:
        """
        Attempts to shorten a proof as much as possible,
        while still keeping the proof valid.
        """
        end = len(self.problem.proof.steps)
        slice_length = 1

        ProofChecker(self.problem).check()

        for i in tqdm(range(len(self.problem.proof.steps), 0, -1)):
            if i > end:
                continue

            slice_length = self.trim_longest_tail(end, slice_length)

            if slice_length > 0:
                del self.trimmed_problem.proof.steps[end - slice_length : end]
                end -= slice_length
                slice_length *= 2
                slice_length = min(slice_length, end)
            else:
                end -= 1
                slice_length = 1

        return self.trimmed_problem.shallow_copy()

    def get_checker_at_step(self, step: int) -> ProofChecker:
        """
        Gets the checker after applying `step` steps.
        If the parameter is 0, for example, this will return the checker before applying any step.
        Note that the proof must be updated every time from the trimmed proof,
        since otherwise the checkpoints are not aware that the end of the proof was trimmed.

        To accelerate getting the checker, I store checkpoints.
        There are many checkpointing strategies. This one stores a single checkpoint every query
        halfway between the last checkpoint and the query. This gives a memory and run-time
        of O(log(N / D)), where D is the number of needed statements of the proof,
        if they are uniformly distributed (Which they are not, and this also improves the run-time).

        I did not give enough thought to the usage:
        We perform a binary search, which gives a more complex access pattern, and might remove too many checkpoints.
        """
        checker = ProofChecker(self.trimmed_problem.shallow_copy())
        checker.load_proof()

        checker.check_until_step(step, skim=True)
        checker.problem = self.trimmed_problem.shallow_copy()
        return checker

    def trim_longest_tail(self, end: int, slice_length: int) -> int:
        """
        Attempts to shorten a proof, by removing a range of steps that ends at the `end` index.
        We begin by trying to remove the range `[end - slice_length : end]`,
        but if this causes the proof to be incorrect, we decrease `slice_length` (exponentially) until the proof is still okay.

        start_checker:  A checker that has skimmed through some amount of steps in the proof (but less than `end - slice_length`).
        end:            The index at which the range we are trying to trim has to end.
        slice_length:   The maximal size of the range that this method will try to remove.

        Returns the length of the range of lines that this method managed to remove.
        """
        while True:
            checker = self.get_checker_at_step(end - slice_length)

            proof_slice = slice(end - slice_length, end)
            if not any([isinstance(step, CommentStep) for step in checker.problem.proof.steps[proof_slice]]):
                del checker.problem.proof.steps[end - slice_length : end]
                try:
                    checker.check_steps()
                    checker.check_proof_finished()
                    return slice_length
                except ProofCheckError:
                    pass
            if slice_length > 1:
                slice_length = slice_length // 2
            else:
                return 0


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Trims proofs to be as short as possible.')
    parser.add_argument('path', help='The path of the proof file to trim.', type=Path)
    parser.add_argument(
        '--overwrite',
        help='Overwrite the file with the trimmed proof when trimming is complete.',
        action='store_true',
    )

    args = parser.parse_args()

    document = GeometryDocument.open(args.path)
    problem = DocumentReader().read(document, read_proof_body=True)

    if problem.embedding is not None:
        collector = NonDegeneracyPredicateCollector()
        non_degenerecy_predicates = collector.collect(problem.statement.assumption_objects, problem.embedding)
        problem.statement.auxiliary_predicates.extend(non_degenerecy_predicates)

    start_time = time.time()
    trimmer = ProofTrimmer(problem)
    trimmed_problem = trimmer.trim()

    DocumentWriter().write_sections(trimmed_problem, document, DocumentSection.PROOF)

    if args.overwrite:
        document.save()
    else:
        for line in document.get_section_content(DocumentSection.PROOF):
            print(line)

    print(f'Trimmed in {round(time.time() - start_time, 2)} seconds')
