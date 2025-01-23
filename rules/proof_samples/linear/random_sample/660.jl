Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, A)
g == Line(B, C)
D == projection(C, f)
c == Circle(A, C, D)
E == projection(A, g)
F == center(c)
G == midpoint(D, A)
H == midpoint(E, C)

Need to prove:
concyclic(B, F, G, H)

Proof:
