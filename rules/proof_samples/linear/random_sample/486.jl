Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
f == Line(B, C)
c == Circle(C, A, B)
D == center(c)
d == Circle(B, C, D)
E == center(d)
F == projection(E, f)
G == midpoint(D, A)

Need to prove:
concyclic(A, E, F, G)

Proof:
