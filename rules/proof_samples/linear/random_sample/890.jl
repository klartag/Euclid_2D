Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
A in c
B in c
C in c
f == Line(A, B)
g == Line(B, C)
D == center(c)
h == parallel_line(D, g)
E == projection(C, h)
F == projection(C, f)
G == midpoint(F, A)

Need to prove:
concyclic(B, C, E, G)

Proof:
