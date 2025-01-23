Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
A in c
B in c
C in c
f == Line(A, B)
g == internal_angle_bisector(C, B, A)
D == projection(C, g)
h == Line(C, D)
E in g, c
F == line_intersection(h, f)
G == midpoint(F, A)

Need to prove:
concyclic(D, E, F, G)

Proof:
