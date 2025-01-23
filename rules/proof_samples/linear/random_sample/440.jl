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
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
J == midpoint(C, A)
K == midpoint(B, A)
c == Circle(I, A, J)
L == center(c)
j == parallel_line(L, f)
k == internal_angle_bisector(H, G, K)
M == line_intersection(k, j)

Need to prove:
concyclic(D, I, J, M)

Proof:
