Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == internal_angle_bisector(A, B, C)
D == projection(A, g)
E == midpoint(C, A)
h == external_angle_bisector(D, E, A)
F == line_intersection(h, f)
c == Circle(B, F, E)
G == center(c)

Need to prove:
concyclic(B, C, E, G)

Proof:
