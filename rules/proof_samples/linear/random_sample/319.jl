Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, A)
D == midpoint(B, C)
g == parallel_line(C, f)
E == midpoint(D, C)
F == midpoint(E, B)
c == Circle(F, C, A)
G in g, c
H == midpoint(G, A)

Need to prove:
concyclic(A, D, F, H)

Proof:
