Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
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
H == midpoint(G, C)
I == midpoint(B, C)
J == midpoint(C, A)
c == Circle(J, H, F)
d == Circle(B, I, F)
K == center(c)
L == center(d)
M in j, d

Need to prove:
concyclic(F, K, L, M)

Proof:
