Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
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
I == midpoint(B, C)
J == midpoint(C, A)
K == midpoint(F, B)
c == Circle(K, C, A)
d == Circle(H, C, F)
L in c, d

Need to prove:
concyclic(C, I, J, L)

Proof:
