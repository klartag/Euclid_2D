Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G)
D == midpoint(B, A)
E == midpoint(D, A)
c == Circle(C, B, E)
F == center(c)
f == Line(F, B)
G == projection(A, f)

Need to prove:
concyclic(D, E, F, G)

Proof:
