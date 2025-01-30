Assumptions:
A, B, C, D, X, Y, Z, W: Point
distinct(A, B, C, D, W, X, Y, Z)
distinct(Line(A, B), Line(A, D), Line(B, C), Line(C, D), Line(W, X), Line(W, Z), Line(X, Y), Line(Y, Z))
collinear(A, X, Y)
collinear(B, Y, Z)
collinear(C, W, Z)
collinear(D, W, X)
Line(X, Y) == external_angle_bisector(B, A, D)
Line(Y, Z) == external_angle_bisector(A, B, C)
Line(W, Z) == external_angle_bisector(B, C, D)
Line(W, X) == external_angle_bisector(A, D, C)

Need to prove:
concyclic(W, X, Y, Z)

Proof:
