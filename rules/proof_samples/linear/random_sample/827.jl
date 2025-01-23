Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N)
distinct(f, g, h, i, j, k, l, m)
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
H == midpoint(G, B)
I == midpoint(B, C)
J == midpoint(C, A)
K == midpoint(B, A)
l == Line(J, H)
m == internal_angle_bisector(K, J, I)
L == line_intersection(k, m)
c == Circle(L, F, J)
M == center(c)
N in l, c

Need to prove:
collinear(N, M, D)

Proof:
