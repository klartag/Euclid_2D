Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
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
I == midpoint(C, A)
J == midpoint(B, A)
c == Circle(G, B, H)
d == Circle(G, C, I)
K in d, c
L == midpoint(A, K)

Need to prove:
collinear(L, J, I)

Proof:
