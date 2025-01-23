Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, C)
g == Line(C, A)
D == midpoint(C, A)
E == midpoint(C, D)
F == midpoint(D, B)
G == projection(F, f)
H == projection(G, g)

Need to prove:
concyclic(E, F, G, H)

Proof:
