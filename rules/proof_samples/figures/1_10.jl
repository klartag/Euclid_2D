Assumptions:
A, B, C, D, E, O, M: Point
distinct(A, B, C, D, E, O, M)
not_collinear(A, B, C)
collinear(A, D, B)
collinear(A, E, C)
concyclic(B, C, E, D)
O == center(Circle(A, D, E))

Need to prove:
perpendicular(Line(A, O), Line(B, C))

Proof:
