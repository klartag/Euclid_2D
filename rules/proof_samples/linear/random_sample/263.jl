Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
j == external_angle_bisector(B, E, C)
k == external_angle_bisector(D, C, A)
l == external_angle_bisector(C, D, E)

Need to prove:
concurrent(j, k, l)

Proof:
