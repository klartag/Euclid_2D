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
I == midpoint(B, C)
J == midpoint(B, A)
c == Circle(G, C, J)
d == Circle(I, E, D)
K == center(c)
L == midpoint(A, H)
M == center(d)

Need to prove:
collinear(L, M, K)

Proof:
