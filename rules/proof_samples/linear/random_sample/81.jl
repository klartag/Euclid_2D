Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(A, F)
H == midpoint(C, F)
I == midpoint(B, C)
J == midpoint(B, A)
c == Circle(D, I, H)
k == Line(I, G)
K == center(c)
L == line_intersection(f, k)

Need to prove:
concyclic(E, J, K, L)

Proof:
