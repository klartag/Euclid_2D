Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h)
f == Line(B, A)
g == Line(B, C)
D == projection(A, g)
E == projection(C, f)
F == midpoint(B, C)
G == midpoint(B, A)
H in g
h == Line(H, E)
c == Circle(D, G, E)
I == midpoint(H, D)
J in h, c
K == midpoint(H, E)

Need to prove:
concyclic(F, I, J, K)

Proof:
