Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l, m, n: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l, m, n)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
j == external_angle_bisector(B, A, D)
F == line_intersection(j, h)
k == internal_angle_bisector(B, D, F)
l == parallel_line(E, j)
m == external_angle_bisector(C, B, E)
G == projection(C, l)
n == Line(C, G)

Need to prove:
concurrent(k, m, n)

Proof:
