Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(D, B, A)
E == midpoint(C, D)
g == Line(C, D)
F in f, d
G in g, d
H == projection(D, f)

Need to prove:
concyclic(E, F, G, H)

Proof:
