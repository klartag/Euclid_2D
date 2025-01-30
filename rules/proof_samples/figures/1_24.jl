Assumptions:
A, B, C, D, X, Y, Z, W, P: Point
c: Circle
distinct(A, B, C, D, X, Y, Z, W, P)
A, B, C, D, X, Y, Z, W in c

distance(A, X) == distance(B, X)
distance(B, Y) == distance(C, Y)
distance(C, Z) == distance(D, Z)
distance(D, W) == distance(A, W)

convex(A, X, B, Y, C, Z, D, W)

Need to prove:
perpendicular(Line(X, Z), Line(Y, W))

Proof:
