Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == external_angle_bisector(A, C, B)
c == Circle(C, A, B)
D == midpoint(B, A)
E in g, c
F == line_intersection(f, g)
d == Circle(A, B, E)
G == midpoint(D, B)
h == Line(E, G)
H in h, d

Need to prove:
concyclic(C, F, G, H)

Proof:
