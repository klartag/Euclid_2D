Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, C)
I == midpoint(B, C)
J == midpoint(C, A)
K == midpoint(B, A)
L == midpoint(I, J)
j == Line(L, C)
M == projection(H, j)

Need to prove:
concyclic(D, G, K, M)

Proof:
