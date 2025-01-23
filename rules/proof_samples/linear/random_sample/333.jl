Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
E == midpoint(C, A)
F == midpoint(B, C)
d == Circle(B, E, A)
G == center(d)
H == projection(G, f)
g == Line(F, E)
I in g, d

Need to prove:
concyclic(D, F, H, I)

Proof:
