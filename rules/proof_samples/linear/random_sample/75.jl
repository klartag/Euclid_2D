Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(C, A)
g == external_angle_bisector(A, B, C)
h == internal_angle_bisector(A, B, C)
c == Circle(C, A, B)
D == line_intersection(f, h)
E in g, c
F == midpoint(C, A)
E in i # (defining i)
G == projection(D, i)

Need to prove:
concyclic(B, D, F, G)

Proof:
