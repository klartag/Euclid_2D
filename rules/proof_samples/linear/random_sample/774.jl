Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(B, C)
g == Line(A, B)
D == center(c)
d == Circle(D, A, C)
E == center(d)
F in g, d
h == parallel_line(F, f)
G in h, d

Need to prove:
collinear(D, G, E)

Proof:
