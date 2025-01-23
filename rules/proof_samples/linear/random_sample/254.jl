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
k == Line(C, F)
G == line_intersection(i, j)
c == Circle(E, D, F)
H in h, c
I in k, c
l == Line(I, H)
J in g
K == midpoint(G, D)
L == projection(J, l)

Need to prove:
concyclic(D, I, K, L)

Proof:
