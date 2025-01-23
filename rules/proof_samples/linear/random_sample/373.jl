Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(B, A)
F == center(c)
d == Circle(E, D, F)
h == Line(E, C)
G in c, d

Need to prove:
G in h

Proof:
