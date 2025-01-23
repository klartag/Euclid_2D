Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
D == midpoint(C, A)
E == midpoint(B, A)
g == parallel_line(D, f)
c == Circle(A, C, E)
h == Line(B, D)
F == projection(B, g)
G == projection(E, h)
d == Circle(E, B, F)
H in d, c

Need to prove:
concyclic(C, D, G, H)

Proof:
