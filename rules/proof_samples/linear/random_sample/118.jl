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
E in f
F == midpoint(D, E)
G == midpoint(E, B)
d == Circle(D, B, A)
g == Line(G, D)
H == center(d)
I == projection(H, g)

Need to prove:
concyclic(A, F, G, I)

Proof:
