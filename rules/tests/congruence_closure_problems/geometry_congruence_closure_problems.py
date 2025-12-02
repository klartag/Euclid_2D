from ...geometry_objects.atom import Atom
from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.literal import Literal
from ...predicates.predicate import Predicate
from ...predicates.loader.pred_config import load_constructions_and_macros

from ...proof.document.geometry_document import GeometryDocument
from ...proof.document.reader.document_reader import DocumentReader

from ...geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker

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
''',
'''
Assumptions:
A, B, C, D, E, F, M: Point

D == midpoint(B, C)
E == midpoint(C, A)
F == midpoint(A, B)

M == line_intersection(Line(A, D), Line(B, E))
M == line_intersection(Line(C, F), Line(A, D))
M == line_intersection(Line(B, E), Line(C, F))
M == centroid(A, B, C)
M == centroid(D, E, F)

Need to prove:
centroid(midpoint(B, A), midpoint(B, C), E) == centroid(F, midpoint(A, C), D)
centroid(A, B, C) == centroid(midpoint(A, B), midpoint(B, C), midpoint(A, C))
'''
]

load_constructions_and_macros()

GEOMETRY_CONGRUENCE_PROBLEMS: list[CongruenceClosureProblem[Atom | Literal, GeoObject, str | EqOp, Predicate]] = []

for problem_statement in _GEOMETRY_CONGRUENCE_PROBLEMS:
    problem = DocumentReader().read(GeometryDocument.from_text(problem_statement), False)
    if problem.statement is not None:
        GEOMETRY_CONGRUENCE_PROBLEMS.append(
            CongruenceClosureProblem(CongruenceClosureTracker, problem.statement.assumption_predicates, problem.statement.target_predicates)
        )
