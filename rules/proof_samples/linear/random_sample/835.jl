Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
c == Circle(C, A, B)
D == center(c)
f == internal_angle_bisector(C, D, A)
d == Circle(A, B, D)
E in f, d
F == midpoint(B, E)
G == midpoint(E, C)

Need to prove:
collinear(G, F, B)

Proof:
