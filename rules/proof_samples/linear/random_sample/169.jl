Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(C, A)
c == Circle(C, A, B)
h == internal_angle_bisector(A, B, C)
i == external_angle_bisector(C, A, B)
D == line_intersection(h, g)
E in i, c
j == Line(E, B)
d == Circle(D, A, E)
e == Circle(C, B, D)
F in f, d
G in j, e

Need to prove:
concyclic(A, C, F, G)

Proof:
