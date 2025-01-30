Assumptions:
A, B, C, D, X, Y, Z, W: Point
distinct(A, B, C, D, X, Y, Z, W)
distinct(Line(X, Y), Line(Y, Z), Line(Z, W), Line(W, X))

not_collinear(A, B, C)
not_collinear(A, B, D)
not_collinear(A, C, D)
not_collinear(B, C, D)

X == midpoint(A, B)
Y == midpoint(B, C)
Z == midpoint(C, D)
W == midpoint(D, A)

Need to prove:
parallelogram(X, Y, Z, W)

Proof:
