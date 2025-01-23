Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
J == midpoint(C, A)
K == midpoint(G, J)
L == midpoint(I, G)
M == midpoint(A, H)

Need to prove:
concyclic(G, K, L, M)

Proof:
