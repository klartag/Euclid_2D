Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
k == Line(E, F)
l == parallel_line(C, k)
m == external_angle_bisector(C, A, G)

Need to prove:
concurrent(j, l, m)

Proof:
