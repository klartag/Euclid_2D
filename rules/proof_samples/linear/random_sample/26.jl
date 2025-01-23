Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
F == midpoint(B, C)
G == midpoint(C, A)
H == midpoint(B, A)
c == Circle(H, F, E)
I == midpoint(H, C)
h == Line(H, C)
J == midpoint(G, D)
K in h, c

Need to prove:
concyclic(D, I, J, K)

Proof:
