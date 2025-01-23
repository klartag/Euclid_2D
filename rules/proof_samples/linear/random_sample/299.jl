Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(B, F)
H == midpoint(C, F)
I == midpoint(B, C)
J == midpoint(H, B)
K == projection(G, f)
k == Line(K, G)
L in k
M == midpoint(L, I)

Need to prove:
collinear(M, I, J)

Proof:
