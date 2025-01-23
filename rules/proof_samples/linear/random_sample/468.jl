Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O)
distinct(f, g, h, i, j, k, l)
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
K == midpoint(B, C)
L == midpoint(C, A)
M == midpoint(B, A)
c == Circle(L, J, A)
N == center(c)
k == parallel_line(N, g)
l == internal_angle_bisector(I, H, M)
O == line_intersection(l, k)

Need to prove:
concyclic(F, K, L, O)

Proof:
