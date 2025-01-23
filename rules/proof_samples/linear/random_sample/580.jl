Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == Line(B, C)
c == Circle(C, A, B)
D == midpoint(C, A)
g == external_angle_bisector(D, A, B)
E in g, c
F == midpoint(A, E)
d == Circle(E, F, C)
G == projection(E, f)
e == Circle(D, G, C)
H in d, e

Need to prove:
collinear(F, H, D)

Proof:
