Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
j == Line(E, F)
G == line_intersection(j, h)
H == midpoint(B, A)
I == midpoint(F, A)
J == midpoint(B, I)

Need to prove:
collinear(H, J, G)

Proof:
