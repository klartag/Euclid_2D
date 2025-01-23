Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k, l)
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
J == midpoint(B, C)
c == Circle(J, I, E)
K == center(c)
k == Line(A, K)
l == Line(I, E)
L == line_intersection(l, k)

Need to prove:
collinear(H, F, L)

Proof:
