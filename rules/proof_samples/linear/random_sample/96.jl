Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
J == midpoint(C, A)
c == Circle(D, J, B)
K == midpoint(B, G)
d == Circle(D, K, H)
L in d, c
M == midpoint(I, K)

Need to prove:
collinear(K, M, L)

Proof:
