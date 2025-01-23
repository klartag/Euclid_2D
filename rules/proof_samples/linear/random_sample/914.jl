Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
H == midpoint(G, A)
I == midpoint(B, C)
J == midpoint(C, A)
c == Circle(J, H, C)
K == projection(I, k)
l == Line(I, K)
L in l, c
M in i, c

Need to prove:
concyclic(G, K, L, M)

Proof:
