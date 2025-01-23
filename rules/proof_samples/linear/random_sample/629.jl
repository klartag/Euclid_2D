Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
f == Line(C, A)
D == projection(B, f)
E == midpoint(C, A)
F == midpoint(E, A)
c == Circle(E, D, B)
G == center(c)
H == midpoint(B, A)

Need to prove:
concyclic(D, F, G, H)

Proof:
