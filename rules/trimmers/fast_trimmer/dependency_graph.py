import argparse
from pathlib import Path

from tqdm import tqdm

from ...theorem import Theorem

from ...geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker
from ...geometry_trackers.linear_algebra_tracker.linear_algebra_tracker import LinearAlgebraTracker
from ...geometry_trackers.linear_algebra_tracker.linear_expression import LinearExpression
from ...geometry_trackers.geometry_tracker import GeometryTracker

from ...predicates.predicate import Predicate

from ...proof.document.geometry_document import GeometryDocument
from ...proof.document.reader.document_reader import DocumentReader
from ...proof.steps.step import Step
from ...proof.steps.theorem_step import TheoremStep
from ...proof.geometry_problem import GeometryProblem

from ...proof_checker import ProofChecker
from ...proof_checker_utils import get_linear_eqn_factors, get_log_eqn_factors, unpack_predicate_full


class DependencyGraph:
    problem: GeometryProblem

    def __init__(self, problem: GeometryProblem):
        self.problem = problem
    
    @property
    def steps(self) -> list[Step]:
        assert self.problem.proof is not None
        return self.problem.proof.steps
    
    def calculate_dependencies(self) -> dict[int, list[int]]:
        ProofChecker(self.problem).check()
        checker = ProofChecker(self.problem)
        checker.load_proof()
        problem_assumption_geometry_tracker = checker.geometry_tracker.clone()
        dependencies: dict[int, list[int]] = {}
        for step_index in tqdm(range(len(self.steps))):
            step = self.steps[step_index]
            if isinstance(step, TheoremStep):
                dependencies[step_index] = self.get_theorem_step_dependencies(problem_assumption_geometry_tracker, checker, step)
            checker.check_steps(1)
        return dependencies
    
    def get_theorem_step_dependencies(self, problem_assumption_geometry_tracker: GeometryTracker, checker: ProofChecker, step: TheoremStep) -> list[int]:
        theorem = Theorem.from_name(step.theorem_name)
        assert theorem is not None
        substitutions = dict(zip(theorem.signature, step.inputs))
        substituted_predicates = [unpacked_predicate for predicate in theorem.required_predicates for unpacked_predicate in unpack_predicate_full(predicate.substitute(substitutions))]
        dependencies: list[int] = []
        for predicate in substituted_predicates:
            if not predicate.is_open():
                explanation_predicates = list(filter(lambda predicate: not problem_assumption_geometry_tracker.contains_predicate(predicate, can_add=False), self.get_predicate_dependencies(checker, predicate))) 
                explanation_steps = list(filter(None, [self.get_step_index_from_predicate(predicate) for explanation_predicate in explanation_predicates]))
                dependencies.extend(explanation_steps)
        return dependencies

    def get_predicate_dependencies(self, checker: ProofChecker, predicate: Predicate) -> list[Predicate]:
        equality_tracker_dependencies = self.get_equality_tracker_dependencies(checker.geometry_tracker.equality_tracker, predicate)
        if equality_tracker_dependencies is not None:
            return equality_tracker_dependencies
        linear_tracker_dependencies = self.get_linear_predicate_dependencies(checker.geometry_tracker._linear_algebra, predicate)
        if linear_tracker_dependencies is not None:
            return linear_tracker_dependencies
        raise Exception(f"Could not find dependencies for the predicate {predicate}")

    def get_linear_predicate_dependencies(self, linear_tracker: LinearAlgebraTracker, predicate: Predicate) -> list[Predicate] | None:
        if predicate.name not in ['equals', 'equals_mod_360']:
            return None
        factors = get_linear_eqn_factors(predicate)
        if factors is None:
            factors = get_log_eqn_factors(predicate)
        if factors is None:
            return None

        linear_expression = LinearExpression(factors)        
        return linear_tracker.explain_relation(linear_expression)

    def get_equality_tracker_dependencies(self, congruence_closure_tracker: CongruenceClosureTracker, predicate: Predicate) -> list[Predicate] | None:
        if congruence_closure_tracker.are_congruent(predicate, True):
            return congruence_closure_tracker.explain(predicate, True)
        
        if predicate.name == 'equals':
            left, right = predicate.components
            if congruence_closure_tracker.are_congruent(left, right):
                return congruence_closure_tracker.explain(left, right)
        
        return None
    
    def get_step_index_from_predicate(self, predicate: Predicate) -> int | None:
        for i, step in enumerate(self.steps):
            if isinstance(step, TheoremStep):
                if predicate in step.result_predicates:
                    return i
        print(f">> {predicate}")
        return None
        raise Exception(f"Could not find the predicate {predicate} in the proof steps.")


def main():
    parser = argparse.ArgumentParser(description='Verifies that proofs are correct.')
    parser.add_argument('path', help='The path of the problem file to verify.', type=Path)
    args = parser.parse_args()

    document = GeometryDocument.open(args.path)
    problem = DocumentReader().read(document, read_proof_body=True)
    graph = DependencyGraph(problem).calculate_dependencies()
    
    assert problem.proof is not None
    
    step_texts = [f'{f"{i}:":<6}{step.to_language_format()}' for i, step in enumerate(problem.proof.steps)]
    
    for i in range(len(problem.proof.steps)):
        print(step_texts[i])
        for j in graph.get(i, []):
            print(f'\t', step_texts[j])
