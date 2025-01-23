Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
d == Circle(E, B, D)
j == external_angle_bisector(D, E, C)
F in j, d
e == Circle(F, D, C)
G in j, e

Need to prove:
concyclic(A, C, E, G)

Proof:
