Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
j == external_angle_bisector(E, A, D)
k == Line(B, D)
l == internal_angle_bisector(B, E, C)
F in k
m == external_angle_bisector(F, D, A)

Need to prove:
concurrent(j, l, m)

Proof:
