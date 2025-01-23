Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
f == Line(C, A)
D == midpoint(B, C)
g == parallel_line(B, f)
d == Circle(A, C, D)
E == midpoint(A, B)
F == center(c)
G == center(d)
H == projection(G, g)

Need to prove:
concyclic(D, E, F, H)

Proof:
