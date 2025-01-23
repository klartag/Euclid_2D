Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(C, A, B)
i == external_angle_bisector(D, B, A)
E == projection(D, i)
j == Line(E, D)
F == line_intersection(h, j)

Need to prove:
concyclic(A, B, C, F)

Proof:
