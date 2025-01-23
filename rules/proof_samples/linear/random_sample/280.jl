Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
A in c
B in c
C in c
f == Line(A, B)
g == Line(C, A)
D == center(c)
E == projection(C, f)
h == Line(E, C)
d == Circle(B, C, E)
F == projection(B, g)
i == parallel_line(F, h)
G in i, d

Need to prove:
collinear(B, D, G)

Proof:
