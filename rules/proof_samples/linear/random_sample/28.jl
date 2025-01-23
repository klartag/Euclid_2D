Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(G, C)
I == midpoint(B, C)
J == projection(I, h)
K == midpoint(H, A)
k == Line(H, A)
L == projection(C, k)

Need to prove:
concyclic(F, J, K, L)

Proof:
