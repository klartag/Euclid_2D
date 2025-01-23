Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
D == midpoint(B, C)
f == external_angle_bisector(C, A, B)
E == midpoint(D, B)
g == internal_angle_bisector(A, C, E)
h == internal_angle_bisector(A, B, C)
F == projection(A, g)
i == Line(F, A)
j == parallel_line(C, i)

Need to prove:
concurrent(f, h, j)

Proof:
