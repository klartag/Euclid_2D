Assumptions:
A, B, C, D, E, F, G, H, I: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(c, d)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
E == midpoint(B, A)
F == midpoint(C, D)
G == projection(C, f)
d == Circle(C, E, D)
H in f, d
I == midpoint(G, E)

Need to prove:
concyclic(C, F, H, I)

Proof:
