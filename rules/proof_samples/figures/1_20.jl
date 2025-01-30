Assumptions:
A, B, C, D, X, Y, Z, W, T: Point
distinct(A, B, C, D, X, Y, Z, W, T)
distinct(Line(X, Y), Line(Y, Z), Line(Z, W), Line(W, X))

not_collinear(A, B, C)
not_collinear(A, B, D)
not_collinear(A, C, D)
not_collinear(B, C, D)

X == midpoint(A, B)
Y == midpoint(B, C)
Z == midpoint(C, D)
W == midpoint(D, A)

T == line_intersection(Line(X, Z), Line(Y, W))

Need to prove:
distance(X, T) == distance(Z, T)
distance(Y, T) == distance(W, T)

Proof:
