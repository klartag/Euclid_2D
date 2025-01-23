Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
D == line_intersection(h, g)
E == projection(D, f)
F == midpoint(B, C)
G == midpoint(A, E)
H == midpoint(F, G)

Need to prove:
collinear(G, D, H)

Proof:
