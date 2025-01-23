Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
c == Circle(C, A, B)
f == external_angle_bisector(A, B, C)
g == internal_angle_bisector(A, B, C)
D == midpoint(C, A)
E in f, c
h == Line(E, D)
F == line_intersection(h, g)

Need to prove:
concyclic(A, B, E, F)

Proof:
