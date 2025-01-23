Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
distinct(c, d)
B in f # (defining f)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
H == midpoint(B, F)
k == Line(B, F)
I in k, c
d == Circle(D, E, F)
J in k, d
K == midpoint(I, C)

Need to prove:
concyclic(E, H, J, K)

Proof:
