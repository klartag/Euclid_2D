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
G == midpoint(C, A)
H == midpoint(B, A)
I == midpoint(A, F)
h == Line(A, F)
c == Circle(D, G, E)
J in h, c
K == midpoint(E, A)

Need to prove:
concyclic(H, I, J, K)

Proof:
