Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(A, G)
I == midpoint(G, C)
J == midpoint(C, A)
K == midpoint(B, A)
c == Circle(K, F, I)
L == midpoint(J, F)
M == center(c)
N == midpoint(H, C)

Need to prove:
concyclic(J, L, M, N)

Proof:
