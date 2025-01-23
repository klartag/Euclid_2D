Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
D == line_intersection(h, g)
E in f
c == Circle(D, C, E)
F == projection(E, h)
G in g, c
H == midpoint(F, G)

Need to prove:
collinear(E, F, H)

Proof:
