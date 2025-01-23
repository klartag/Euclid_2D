Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
J == midpoint(B, C)
K == midpoint(C, A)
j == external_angle_bisector(I, J, G)
k == internal_angle_bisector(K, H, B)
L == line_intersection(k, j)

Need to prove:
concyclic(G, I, J, L)

Proof:
