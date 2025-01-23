Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == projection(B, f)
E == center(c)
g == external_angle_bisector(B, E, C)
d == Circle(B, E, D)
F == midpoint(B, A)
G in g, d

Need to prove:
collinear(D, G, F)

Proof:
