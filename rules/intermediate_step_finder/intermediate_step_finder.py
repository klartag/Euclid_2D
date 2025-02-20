from typing import List

from pathlib import Path
import time

from tqdm import trange


from ..proof import Proof, TheoremStep
from ..trimmers.trimmer import ProofTrimmer


class IntermediateStepFinder:
    proof: Proof

    def __init__(self, proof: Proof):
        self.proof = proof
        
    def evaluate_all_steps(self) -> List[float]:
        return [self.evaluate_step_worth(i) for i in trange(len(self.proof.steps))]

    
    def evaluate_step_worth(self, step_index: int) -> float:
        proof_clone = self.proof.shallow_copy()
        step = proof_clone.steps[step_index]
        if not isinstance(step, TheoremStep):
            return 0
        proof_clone.assumption_predicates.extend(step.result_predicates)
        trimmer = ProofTrimmer(proof_clone)
        trimmer.trim()
        return 1 - len(trimmer.trimmed_proof.steps) / float(len(proof_clone.steps))

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Does a thing.')
    parser.add_argument('path', help='The path of the proof file to do a thing.', type=Path)

    args = parser.parse_args()
    path = Proof.get_full_proof_path(args.path)
    proof = Proof.parse(path.open().read())

    t0 = time.time()
    step_finder = IntermediateStepFinder(proof)
    evaluations = step_finder.evaluate_all_steps()
    
    for x, y in sorted(zip(proof.steps, evaluations), key=lambda x:x[1]):
        print(x, y)
    print(f'Did a thing in {round(time.time() - t0, 2)} seconds')
