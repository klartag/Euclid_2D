Assumptions:
A, B, C, D, E, F, P, Q: Point
distinct(A, B, C, D, E, F, P, Q)

angle(A, B, C) < 90 mod 360
angle(B, C, A) < 90 mod 360
angle(C, A, B) < 90 mod 360

D == projection(A, Line(B, C))
E == projection(B, Line(A, C))
F == projection(C, Line(A, B))

P in Line(E, F), Circle(A, B, C)
Q in Line(B, P), Line(D, F)

Need to prove:
distance(A, P) == distance(A, Q)

Proof:
