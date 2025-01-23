Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(B, F)
H == midpoint(C, A)
I == midpoint(B, A)
c == Circle(G, H, D)
J == midpoint(F, I)
K == center(c)
L == projection(K, f)

Need to prove:
collinear(K, J, L)

Proof:
