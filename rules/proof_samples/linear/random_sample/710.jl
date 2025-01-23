Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
D == line_intersection(h, g)
E == projection(D, f)
F == projection(C, h)
G == projection(E, h)
i == Line(E, G)
j == parallel_line(F, f)

Need to prove:
concurrent(g, i, j)

Proof:
