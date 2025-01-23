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
h == Line(D, A)
E == midpoint(B, C)
d == Circle(C, A, E)
F in h, d
G == center(c)
H == projection(G, g)

Need to prove:
concyclic(A, F, G, H)

Proof:
