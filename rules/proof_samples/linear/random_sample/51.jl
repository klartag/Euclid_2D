Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(A, B, C)
E == projection(C, j)
F == midpoint(B, D)
c == Circle(F, E, C)
G in j, c

Need to prove:
concyclic(A, B, C, G)

Proof:
