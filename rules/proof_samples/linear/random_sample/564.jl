Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
H == projection(C, j)
c == Circle(H, C, B)
I == projection(E, k)
J == midpoint(F, G)
l == Line(F, G)
K in l, c
L == projection(J, j)

Need to prove:
concyclic(B, I, K, L)

Proof:
