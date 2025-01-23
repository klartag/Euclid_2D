Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
H == projection(A, j)
k == Line(F, G)
I == line_intersection(k, j)
J == midpoint(E, F)

Need to prove:
concyclic(C, H, I, J)

Proof:
