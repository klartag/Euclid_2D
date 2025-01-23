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
E == midpoint(D, B)
F == center(c)
d == Circle(C, B, F)
G in g, d
h == Line(A, G)
H == projection(D, h)

Need to prove:
concyclic(A, B, E, H)

Proof:
