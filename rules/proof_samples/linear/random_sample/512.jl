Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
A in f # (defining f)
g == Line(C, A)
h == external_angle_bisector(A, B, C)
D == line_intersection(h, g)
i == internal_angle_bisector(A, B, C)
c == Circle(B, C, D)
E in i, c
F == projection(E, f)

Need to prove:
concyclic(A, C, E, F)

Proof:
