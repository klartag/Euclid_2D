Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, B)
H == midpoint(F, C)
I == midpoint(B, C)
J == midpoint(C, A)
c == Circle(H, G, I)
K == center(c)
L == midpoint(K, J)

Need to prove:
collinear(L, G, K)

Proof:
