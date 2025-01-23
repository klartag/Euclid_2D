Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
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
I == midpoint(B, G)
J == midpoint(G, C)
K == midpoint(B, A)
c == Circle(H, J, D)
k == Line(K, D)
L == center(c)
l == Line(A, L)
d == Circle(I, L, F)
M in l, d
N == line_intersection(k, l)

Need to prove:
concyclic(D, E, M, N)

Proof:
