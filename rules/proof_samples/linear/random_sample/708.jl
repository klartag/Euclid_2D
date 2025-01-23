Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
D == midpoint(B, A)
E == midpoint(C, D)
f == Line(C, D)
g == parallel_line(B, f)
F == midpoint(D, A)
h == Line(E, A)
i == Line(F, E)
j == parallel_line(C, h)

Need to prove:
concurrent(g, i, j)

Proof:
