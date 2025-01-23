Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, C)
D == projection(A, f)
g == Line(D, A)
E == midpoint(B, A)
F == midpoint(C, A)
G == projection(F, g)

Need to prove:
collinear(F, G, E)

Proof:
