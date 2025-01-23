Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k)
f == Line(C, A)
D == midpoint(B, C)
g == external_angle_bisector(D, C, A)
E == projection(A, g)
h == Line(E, A)
i == parallel_line(C, h)
j == parallel_line(B, g)
k == parallel_line(D, f)

Need to prove:
concurrent(i, j, k)

Proof:
