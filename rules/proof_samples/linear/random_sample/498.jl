Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(D, A)
F == midpoint(B, A)
G == midpoint(C, A)
h == Line(C, F)
d == Circle(D, C, E)
H in h, d

Need to prove:
concyclic(E, F, G, H)

Proof:
