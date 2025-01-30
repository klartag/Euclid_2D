Assumptions:
A, B, C, D, X: Point
distinct(A, B, C, D, X)

concyclic(A, B, C, D)

X == line_intersection(Line(A, C), Line(B, D))

Need to prove:
distance(A, X) * distance(C, X) == distance(B, X) * distance(D, X)

Proof:
