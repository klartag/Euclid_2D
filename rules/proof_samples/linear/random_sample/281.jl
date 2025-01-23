Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, C)
h == external_angle_bisector(C, D, A)
i == external_angle_bisector(A, D, B)
c == Circle(D, B, A)
E == line_intersection(h, g)
F == line_intersection(i, f)
G in h, c

Need to prove:
concyclic(A, E, F, G)

Proof:
