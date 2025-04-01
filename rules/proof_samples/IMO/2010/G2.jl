Assumptions:
A, B, C, P, K, L, M, S: Point
distinct(A, B, C, P, K, L, M, S)

identical(orientation(P, A, B), orientation(P, B, C), orientation(P, C, A))

K in Line(A, P), Circle(A, B, C)
L in Line(B, P), Circle(A, B, C)
M in Line(C, P), Circle(A, B, C)

S in Line(A, B), point_circle_tangent_line(C, Circle(A, B, C))

distance(S, C) == distance(S, P)

Need to prove:
distance(M, K) == distance(M, L)

Proof:
