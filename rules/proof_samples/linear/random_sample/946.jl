Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, A)
g == Line(B, C)
D == projection(A, g)
E == projection(C, f)
F == midpoint(C, A)
G == midpoint(B, A)
c == Circle(B, E, D)
H == center(c)

Need to prove:
concyclic(E, F, G, H)

Proof:
