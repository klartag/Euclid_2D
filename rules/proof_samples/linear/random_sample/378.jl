Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == parallel_line(C, f)
h == Line(C, A)
D == midpoint(B, A)
E == projection(D, h)
c == Circle(C, E, B)
F in g, c
G == midpoint(F, C)
H == projection(G, h)

Need to prove:
concyclic(A, B, F, H)

Proof:
