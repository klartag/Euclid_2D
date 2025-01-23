Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l, m, n: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l, m, n)
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
l == external_angle_bisector(G, D, E)
m == parallel_line(C, k)
n == parallel_line(B, l)

Need to prove:
concurrent(i, m, n)

Proof:
