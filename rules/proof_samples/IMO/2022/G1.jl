Assumptions:
A, B, C, D, E, P, Q, R, S, T: Point

distinct(A, B, C, D, E, P, Q, R, S, T)

convex(A, B, C, D, E)
distance(B, C) == distance(D, E)
identical(orientation(T, A, B), orientation(T, B, C), orientation(T, C, D), orientation(T, D, E), orientation(T, E, A))

distance(T, B) == distance(T, D)
distance(T, C) == distance(T, E)
angle(T, B, A) == angle(A, E, T) mod 360

P in Line(C, D), Line(A, B)
Q in Line(C, T), Line(A, B)

R in Line(C, D), Line(A, E)
S in Line(D, T), Line(A, E)

between(P, B, A, Q)
between(R, E, A, S)

Need to prove:
concyclic(P, S, Q, R)

Proof:
