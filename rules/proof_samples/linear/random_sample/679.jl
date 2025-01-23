Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(C, A)
h == parallel_line(B, g)
c == Circle(C, A, B)
D in h, c
d == Circle(A, B, D)
E == center(d)
e == Circle(E, A, C)
i == Line(D, C)
F == center(e)
j == Line(E, F)

Need to prove:
concurrent(f, i, j)

Proof:
