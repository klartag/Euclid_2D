Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, B)
H == midpoint(F, C)
I == midpoint(B, C)
J == midpoint(C, A)
K == midpoint(B, A)
j == Line(J, H)
k == Line(I, K)
L == line_intersection(k, i)
M == line_intersection(k, j)

Need to prove:
concyclic(G, H, L, M)

Proof:
