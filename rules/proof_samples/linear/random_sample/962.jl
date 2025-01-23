Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
G == projection(A, i)
H == midpoint(E, G)
I == midpoint(H, F)

Need to prove:
collinear(E, G, I)

Proof:
