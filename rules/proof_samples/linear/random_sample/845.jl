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
I == midpoint(C, A)
J == midpoint(B, A)
K == projection(E, f)
k == Line(E, K)
c == Circle(I, F, J)
d == Circle(H, B, F)
L in k, c
M == center(d)

Need to prove:
collinear(M, L, F)

Proof:
