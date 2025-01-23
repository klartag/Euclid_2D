Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
D == midpoint(B, C)
h == parallel_line(A, g)
E == midpoint(C, A)
F == midpoint(B, E)
i == Line(F, D)
j == parallel_line(E, h)

Need to prove:
concurrent(f, i, j)

Proof:
