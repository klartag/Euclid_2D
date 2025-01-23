Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G)
f == Line(B, A)
D == midpoint(B, C)
E == midpoint(B, A)
F == midpoint(D, C)
c == Circle(E, F, D)
G in f, c

Need to prove:
concyclic(A, C, F, G)

Proof:
