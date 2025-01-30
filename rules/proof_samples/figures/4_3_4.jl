Assumptions:
A, B, C, D, E: Point
distinct(A, B, C, D, E)
not_collinear(A, B, C)
tangent(Line(A, E), Circle(A, B, C))
Line(A, D) == internal_angle_bisector(B, A, C)
D, E in Line(B, C)

Need to prove:
distance(A, E) == distance(D, E)

Proof:
