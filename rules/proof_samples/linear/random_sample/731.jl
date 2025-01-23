Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(D, C)
F == midpoint(B, D)
j == Line(F, C)
k == Line(E, A)
l == parallel_line(D, j)

Need to prove:
concurrent(g, k, l)

Proof:
