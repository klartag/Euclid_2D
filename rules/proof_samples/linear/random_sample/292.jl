Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
D == midpoint(C, A)
E == midpoint(B, A)
F == projection(E, f)
F in h # (defining h)
G == projection(A, h)
c == Circle(D, F, E)
H in g, c

Need to prove:
concyclic(A, F, G, H)

Proof:
