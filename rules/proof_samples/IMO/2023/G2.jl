Assumptions:
A, B, C, D, E, P, Q, S: Point
o: Circle
r: Scalar

distinct(A, B, C, D, E, P, Q, S)
not_collinear(A, B, C)
distance(A, C) > distance(B, C)

o == circumcircle(A, B, C)
r == radius(o)

between(A, P, C)
distance(B, C) == distance(C, P)

S == projection(P, Line(A, B))

collinear_and_not_between(D, B, P)
D in o

Q in Line(S, P)
distance(P, Q) == r
between(S, P, Q)

E == line_intersection(altitude(A, Line(C, Q)), altitude(B, Line(D, Q)))

Need to prove:
E in o

Proof:
