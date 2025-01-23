Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
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
c == Circle(B, D, E)
H == midpoint(F, G)
I == projection(E, k)
J in i, c
K in k, c

Need to prove:
concyclic(H, I, J, K)

Proof:
