Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == projection(C, i)
j == Line(D, C)
E == projection(A, h)
k == Line(E, A)
l == Line(D, E)
F == projection(B, l)
m == Line(F, B)

Need to prove:
concurrent(j, k, m)

Proof:
