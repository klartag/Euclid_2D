from pathlib import Path
import time
from typing import List

from tqdm import tqdm

from ..embeddings.non_degenerecy_predicate_collection.collector import NonDegeneracyPrediateCollector
from ..proof.proof import Proof
from ..proof.steps import CommentStep
from ..proof_checker import ProofChecker
from ..rule_utils import ProofCheckError


class ProofTrimmer:
    proof: Proof
    trimmed_proof: Proof

    def __init__(self, proof: Proof):
        self.proof = proof
        self.trimmed_proof = self.proof.shallow_copy()

    def trim(self) -> Proof:
        """
        Attempts to shorten a proof as much as possible,
        while still keeping the proof valid.
        """
        step = 0
        chunk_size = 1

        ProofChecker(self.proof).check()

        with tqdm(total=len(self.trimmed_proof.steps)) as progress_bar:
            while step < len(self.trimmed_proof.steps):
                trimmed_steps = self.trim_from_step(step, chunk_size)
                if len(trimmed_steps) > 0:
                    for i in trimmed_steps[::-1]:
                        del self.trimmed_proof.steps[i]
                    progress_bar.update(len(trimmed_steps))
                    chunk_size = min(2 * chunk_size, len(self.trimmed_proof.steps) - step)
                elif chunk_size > 1:
                    chunk_size //= 2
                else:
                    step += 1
                    progress_bar.update(1)

        return self.trimmed_proof.shallow_copy()

    def get_checker_at_step(self, step: int) -> ProofChecker:
        """
        Gets the checker after applying `step` steps.
        If the parameter is 0, for example, this will return the checker before applying any step.
        """
        res = ProofChecker(self.trimmed_proof.shallow_copy())
        res.load_proof()

        res.check_until_step(step, skim=True)
        res.proof = self.trimmed_proof.shallow_copy()
        return res

    def trim_from_step(self, step: int, chunk_size: int) -> List[int]:
        """
        Attempts to shorten a proof, by removing the step `step`,
        and then by also removing every proof step that depends on it.

        If by the end of the proof, the `Need to Prove` hasn't been proved,
        we deduce that `step` is required for the proof, and do not trim it.

        Returns the list of steps this method managed to remove.
        """
        removed_steps = [
            i for i in range(step, step + chunk_size) if not isinstance(self.trimmed_proof.steps[i], CommentStep)
        ]

        checker = self.get_checker_at_step(step)
        checker.checked_steps += chunk_size

        while checker.checked_steps < len(checker.proof.steps):
            try:
                checker.check_steps()
            except ProofCheckError:
                removed_steps.append(checker.checked_steps)
                checker.checked_steps += 1
        try:
            checker.check_proof_finished()
            return removed_steps
        except ProofCheckError:
            return []


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
