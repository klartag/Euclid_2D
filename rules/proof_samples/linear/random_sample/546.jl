Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == Line(C, A)
D == midpoint(B, C)
c == Circle(C, D, A)
E == projection(B, f)
F == center(c)
d == Circle(B, E, A)
G == center(d)
H == projection(F, f)

Need to prove:
concyclic(D, E, G, H)

Proof:
