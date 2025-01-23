Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k)
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
H == midpoint(B, G)
I == midpoint(G, C)
J == midpoint(B, A)
c == Circle(D, I, H)
d == Circle(B, J, E)
K == center(d)
L == projection(F, j)
k == Line(L, F)
M in k, c

Need to prove:
collinear(M, K, E)

Proof:
