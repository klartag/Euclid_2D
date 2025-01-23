Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, A)
E == center(c)
d == Circle(A, E, D)
F == center(d)
G == midpoint(E, B)
f == Line(E, B)
H in f, d

Need to prove:
concyclic(D, F, G, H)

Proof:
