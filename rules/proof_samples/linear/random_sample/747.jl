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
h == parallel_line(A, g)
d == Circle(D, C, A)
E == center(d)
i == parallel_line(D, h)
F in f, d
G in i, d

Need to prove:
collinear(G, E, F)

Proof:
