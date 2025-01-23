Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(B, h)
E == projection(C, f)
F == midpoint(D, A)
G == midpoint(B, E)
c == Circle(G, A, C)
H in g, c

Need to prove:
concyclic(C, E, F, H)

Proof:
