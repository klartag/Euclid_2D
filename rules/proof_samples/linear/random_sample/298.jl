Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e, h: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e, h)
f == Line(B, A)
g == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(B, C, D)
E in g, d
e == Circle(A, E, B)
F == projection(E, f)
G == center(e)
h == Circle(F, A, E)
H == center(h)

Need to prove:
concyclic(A, F, G, H)

Proof:
