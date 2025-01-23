Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
c == Circle(C, A, B)
D == center(c)
d == Circle(D, C, A)
h == parallel_line(E, f)
F == projection(D, h)
i == Line(D, F)
G in i, d

Need to prove:
G in g

Proof:
