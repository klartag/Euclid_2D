from ...proof.document.geometry_document import GeometryDocument
from ...proof.document.reader.document_reader import DocumentReader

from ...geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker

from ...predicates.loader.pred_config import load_constructions_and_macros

from .congruence_closure_problem import CongruenceClosureProblem


_GEOMETRY_CONGRUENCE_PROBLEMS: list[str] = [
'''
Assumptions:
A, B, C, A1, A2, B1, B2, C1, C2: Point
c: Circle

c == Circle(A, B, C)
A == midpoint(A1, A2)
B == midpoint(B1, B2)
C == midpoint(C1, C2)

Need to prove:
c == Circle(midpoint(B2, B1), midpoint(C2, C1), midpoint(A2, A1))
c == Circle(midpoint(C2, C1), midpoint(B2, B1), midpoint(A2, A1))
c == Circle(midpoint(B2, B1), midpoint(A1, A2), midpoint(C2, C1))
'''
]

load_constructions_and_macros()

GEOMETRY_CONGRUENCE_PROBLEMS = []

for problem_statement in _GEOMETRY_CONGRUENCE_PROBLEMS:
    problem = DocumentReader().read(GeometryDocument.from_text(problem_statement), False)
    if problem.statement is not None:
        GEOMETRY_CONGRUENCE_PROBLEMS.append(
            CongruenceClosureProblem(CongruenceClosureTracker, problem.statement.assumption_predicates, problem.statement.target_predicates)
        )
