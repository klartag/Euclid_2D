Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(A, B, C)
E == projection(D, j)
k == Line(D, E)
l == external_angle_bisector(D, A, C)
m == external_angle_bisector(D, C, A)

Need to prove:
concurrent(k, l, m)

Proof:
