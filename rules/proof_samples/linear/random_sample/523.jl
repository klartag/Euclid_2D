Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
j == parallel_line(E, h)
F == projection(B, j)
k == Line(B, F)
l == parallel_line(E, k)

Need to prove:
concurrent(g, i, l)

Proof:
