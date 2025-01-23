Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
distinct(c, d)
A in c
B in c
C in c
f == Line(A, B)
g == Line(C, A)
D == center(c)
d == Circle(C, B, D)
h == parallel_line(C, f)
E == projection(D, h)
i == Line(E, D)
F in i, d

Need to prove:
F in g

Proof:
