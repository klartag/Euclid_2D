Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
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
J == midpoint(C, A)
K == midpoint(B, A)
L == midpoint(H, K)
k == parallel_line(K, g)
c == Circle(I, K, L)
M in k, c

Need to prove:
concyclic(F, J, L, M)

Proof:
