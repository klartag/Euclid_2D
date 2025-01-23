Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h)
distinct(c, d, e, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
c == Circle(B, D, A)
d == Circle(D, C, A)
E == midpoint(D, A)
F == center(d)
G in f, d
e == Circle(G, D, F)
k == Circle(A, E, F)
H == center(k)
I in h, e
J in k, c
K == center(c)

Need to prove:
concyclic(H, I, J, K)

Proof:
