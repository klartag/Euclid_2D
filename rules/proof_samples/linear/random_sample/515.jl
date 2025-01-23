Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
D == projection(C, f)
c == Circle(A, C, D)
E in g, c
d == Circle(E, D, B)
F == center(c)
G == midpoint(B, A)
H == center(d)

Need to prove:
concyclic(D, F, G, H)

Proof:
