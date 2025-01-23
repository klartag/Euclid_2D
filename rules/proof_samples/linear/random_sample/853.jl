Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
F in h
d == Circle(C, B, E)
e == Circle(E, A, F)
G in e, d
H == midpoint(F, B)

Need to prove:
collinear(H, B, G)

Proof:
