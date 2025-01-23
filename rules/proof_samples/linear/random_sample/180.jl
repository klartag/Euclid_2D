Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(C, A)
D == projection(B, g)
E == projection(C, f)
h == Line(D, B)
i == Line(E, C)
c == Circle(C, A, B)
j == parallel_line(B, i)
F in j, c
k == parallel_line(F, h)

Need to prove:
concurrent(g, i, k)

Proof:
