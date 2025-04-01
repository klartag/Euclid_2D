Assumptions:
A, B, C, H, W, M, N, X, Y: Point
c, d: Circle
distinct(A, B, C, H, W, M, N, X, Y)

acute_triangle(A, B, C)

H == orthocenter(A, B, C)
between(B, W, C)

M == projection(B, Line(A, C))
N == projection(C, Line(A, B))

c == Circle(B, W, N)
center(c) == midpoint(X, W)

d == Circle(C, W, M)
center(d) == midpoint(Y, W)

Need to prove:
collinear(X, Y, H)

Proof:
