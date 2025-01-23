Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, C)
I == midpoint(B, C)
j == internal_angle_bisector(A, C, H)
J == projection(B, j)

Need to prove:
collinear(G, J, I)

Proof:
