Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, B)
H == midpoint(F, C)
I == midpoint(B, C)
J == midpoint(C, A)
c == Circle(C, I, H)
j == internal_angle_bisector(G, J, A)
K == center(c)
L == projection(K, i)
k == Line(K, L)
M == line_intersection(j, k)

Need to prove:
concyclic(G, I, J, M)

Proof:
