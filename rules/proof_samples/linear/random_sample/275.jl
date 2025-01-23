Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P: Point
f, g, h, i, j, k, l, m: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P)
distinct(f, g, h, i, j, k, l, m)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
H == midpoint(G, A)
I == midpoint(G, B)
J == midpoint(G, C)
K == midpoint(C, A)
L == midpoint(B, A)
c == Circle(H, E, L)
l == parallel_line(H, h)
M == center(c)
d == Circle(J, C, K)
N == center(d)
O == midpoint(C, I)
m == parallel_line(O, l)
P == line_intersection(k, m)

Need to prove:
concyclic(J, M, N, P)

Proof:
