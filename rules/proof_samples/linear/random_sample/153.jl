Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
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
c == Circle(G, B, C)
H in f, c
d == Circle(D, C, G)
I == projection(H, h)
J == center(c)
k == Line(I, G)
K == center(d)
L == projection(B, k)

Need to prove:
concyclic(F, J, K, L)

Proof:
