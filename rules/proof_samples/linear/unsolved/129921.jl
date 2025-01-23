Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P: Point
f, g, h, i, j, k, l, m: Line
c, d, e, p, q: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P)
distinct(f, g, h, i, j, k, l, m)
distinct(c, d, e, p, q)
A in c
B in c
C in c
D in c
f == Line(A, B)
g == Line(B, C)
h == Line(C, D)
E == midpoint(C, D)
F == midpoint(A, D)
G == midpoint(A, B)
H == midpoint(B, C)
i == Line(A, D)
j == parallel_line(E, f)
k == parallel_line(F, g)
l == parallel_line(G, h)
m == parallel_line(H, i)
I == line_intersection(k, j)
J == line_intersection(l, k)
K == line_intersection(m, l)
L == line_intersection(j, m)
d == Circle(J, F, G)
e == Circle(K, G, H)
p == Circle(H, E, L)
q == Circle(E, I, F)
M == center(e)
N == center(p)
O == center(q)
P == center(d)

Need to prove:
concyclic(M, N, O, P)

Proof:
