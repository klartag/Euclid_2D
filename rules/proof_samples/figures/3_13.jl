Assumptions:
A, B, C, D, E, F, P: Point
distinct(A, B, C, D, E, F, P)

P in Circle(A, B, C)

D in Line(B, C)
E in Line(A, C)
F in Line(A, B)

coangle(P, D, B) == coangle(P, E, C) mod 360
coangle(P, D, B) == coangle(P, F, A) mod 360

Need to prove:
collinear(D, E, F)

Proof:
