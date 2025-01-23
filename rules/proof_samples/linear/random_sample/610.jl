Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(A, G)
I == midpoint(B, G)
c == Circle(C, E, I)
J == midpoint(F, A)
k == Line(H, I)
K in k, c

Need to prove:
concyclic(F, H, J, K)

Proof:
