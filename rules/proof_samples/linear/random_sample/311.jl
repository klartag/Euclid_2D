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
j == Line(C, A)
k == internal_angle_bisector(B, C, D)
l == Line(B, D)
E == projection(D, k)
m == parallel_line(E, i)

Need to prove:
concurrent(j, l, m)

Proof:
