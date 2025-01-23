Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
h == parallel_line(B, g)
D == projection(A, h)
c == Circle(D, C, A)
E in h, c
F in f, c
G == center(c)
H == midpoint(B, C)

Need to prove:
concyclic(E, F, G, H)

Proof:
