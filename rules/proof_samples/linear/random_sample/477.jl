Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
c == Circle(C, A, B)
D == center(c)
E == midpoint(B, A)
F == midpoint(C, A)
h == parallel_line(D, f)
d == Circle(E, D, F)
G == projection(F, g)
H in h, d

Need to prove:
concyclic(A, B, G, H)

Proof:
