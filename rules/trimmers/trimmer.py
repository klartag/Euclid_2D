from pathlib import Path
import time

from tqdm import tqdm

from ..embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPrediateCollector
from ..proof import Proof
from ..proof_checker import ProofChecker
from ..rule_utils import ProofCheckError

MIN_CHECKPOINT_STEPS = 2


class ProofTrimmer:
    proof: Proof
    trimmed_proof: Proof
    checkpoints: list[ProofChecker]

    def __init__(self, proof: Proof):
        self.proof = proof
        self.trimmed_proof = self.proof.shallow_copy()
        self.checkpoints = []

    def trim(self) -> Proof:
        """
        Attempts to shorten a proof as much as possible,
        while still keeping the proof valid.
        """
        end = len(self.proof.steps)
        slice_length = 1

        ProofChecker(self.proof).check()

        for i in tqdm(range(len(self.proof.steps), 0, -1)):
            if i > end:
                continue

            slice_length = self.trim_longest_tail(end, slice_length)

            if slice_length > 0:
                del self.trimmed_proof.steps[end - slice_length : end]
                end -= slice_length
                slice_length *= 2
                slice_length = min(slice_length, end)
            else:
                end -= 1
                slice_length = 1

        return self.trimmed_proof.shallow_copy()

    def trim_with_indices(self) -> Proof:
        """
        Attempts to shorten a proof as much as possible,
        while still keeping the proof valid.
        """

        end = len(self.proof.steps)
        step_indices = set(range(end))
        slice_length = 1

        ProofChecker(self.proof).check()

        for i in tqdm(range(len(self.proof.steps), 0, -1)):
            if i > end:
                continue

            slice_length = self.trim_longest_tail(end, slice_length)

            if slice_length > 0:
                del self.trimmed_proof.steps[end - slice_length : end]
                step_indices -= set(range(end - slice_length, end))
                end -= slice_length
                slice_length *= 2
                slice_length = min(slice_length, end)
            else:
                end -= 1
                slice_length = 1

        return self.trimmed_proof.shallow_copy(), step_indices

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
        # Loading the first checkpoint.
        # if len(self.checkpoints) == 0:
        #     res = ProofChecker(self.trimmed_proof.shallow_copy())
        #     res.load_proof()
        #     self.checkpoints.append(res)

        # while self.checkpoints[-1].checked_steps > step:
        #     self.checkpoints.pop()

        # res = self.checkpoints[-1].shallow_copy()

        res = ProofChecker(self.trimmed_proof.shallow_copy())
        res.load_proof()

        # for _ in range(2):
        #     if (step - res.checked_steps) >= 2 * MIN_CHECKPOINT_STEPS:
        #         checkpoint_step = (res.checked_steps + step) // 2
        #         res.check_until_step(checkpoint_step, skim=True)
        #         self.checkpoints.append(res.shallow_copy())

        res.check_until_step(step, skim=True)
        res.proof = self.trimmed_proof.shallow_copy()
        return res

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
            del checker.proof.steps[end - slice_length : end]
            try:
                checker.check_steps()
                checker.check_proof_finished()
                return slice_length

            except ProofCheckError:
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
    path = Proof.get_full_proof_path(args.path)
    proof = Proof.parse(path.open().read())
    
    if proof.embedding is not None:
        collector = NonDegeneracyPrediateCollector()
        non_degenerecy_predicates = collector.collect(proof.assumption_objects, proof.embedding)
        proof.auxiliary_predicates.extend(non_degenerecy_predicates)

    t0 = time.time()
    trimmer = ProofTrimmer(proof)
    trimmed_proof = trimmer.trim()

    proof_text = trimmed_proof.to_language_format()

    if args.overwrite:
        open(path, 'w').write(proof_text)
    else:
        print(proof_text)

    print(f'Trimmed in {round(time.time() - t0, 2)} seconds')
