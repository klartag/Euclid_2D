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
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(A, G)
I == midpoint(B, G)
J == midpoint(C, A)
k == Line(J, I)
K == line_intersection(i, k)
c == Circle(E, I, H)
L == center(c)

Need to prove:
concyclic(F, H, K, L)

Proof:
