Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, C)
g == Line(C, A)
D == projection(B, g)
E == midpoint(D, A)
c == Circle(D, B, A)
F == center(c)
G == projection(E, f)
H == midpoint(B, C)

Need to prove:
concyclic(E, F, G, H)

Proof:
