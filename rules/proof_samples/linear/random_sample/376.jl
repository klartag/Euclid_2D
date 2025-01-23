Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
D == projection(C, f)
c == Circle(C, B, D)
E == midpoint(B, A)
F == center(c)
g == Line(F, E)
G in g
d == Circle(E, D, G)
H in c, d

Need to prove:
concyclic(C, F, G, H)

Proof:
