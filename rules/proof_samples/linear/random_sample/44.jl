Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
D == midpoint(B, C)
c == Circle(C, A, B)
d == Circle(A, B, D)
g == external_angle_bisector(C, D, A)
E in g, d
F == center(c)
G == projection(F, f)

Need to prove:
collinear(G, E, F)

Proof:
