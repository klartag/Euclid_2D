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
f == Line(A, B)
g == parallel_line(C, f)
D == center(c)
E in g, c
d == Circle(E, D, A)
F in g, d
G == midpoint(F, A)
H == midpoint(E, B)

Need to prove:
concyclic(D, F, G, H)

Proof:
