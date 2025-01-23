Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D == midpoint(C, A)
E == projection(A, g)
i == Line(E, A)
j == parallel_line(D, h)
F == center(c)
k == parallel_line(F, i)

Need to prove:
concurrent(g, j, k)

Proof:
