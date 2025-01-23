Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
G == projection(E, j)
H == midpoint(F, G)

Need to prove:
collinear(F, H, E)

Proof:
