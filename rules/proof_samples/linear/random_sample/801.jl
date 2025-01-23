Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
D == midpoint(C, A)
i == parallel_line(D, g)
j == Line(D, B)
E == midpoint(D, C)
k == parallel_line(E, j)

Need to prove:
concurrent(h, i, k)

Proof:
