Assumptions:
A, B, C, P, Q, M, N, X: Point
distinct(A, B, C, P, Q, M, N)

acute_triangle(A, B, C)

between(B, P, C)
between(B, Q, C)

angle(P, A, B) == angle(A, C, B) mod 360
angle(Q, A, C) == angle(C, B, A) mod 360

collinear_and_not_between(M, A, P)
collinear_and_not_between(N, A, Q)
distance(A, P) == distance(P, M)
distance(A, Q) == distance(Q, N)

X in Line(B, M), Line(C, N)

Need to prove:
X in Circle(A, B, C)

Proof:
