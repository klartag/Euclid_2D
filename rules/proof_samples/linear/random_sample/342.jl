Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(C, A)
h == external_angle_bisector(C, A, B)
i == parallel_line(B, h)
D == line_intersection(i, g)
E == midpoint(D, C)
F == projection(C, i)
j == parallel_line(E, f)
G == line_intersection(j, h)

Need to prove:
concyclic(A, D, F, G)

Proof:
