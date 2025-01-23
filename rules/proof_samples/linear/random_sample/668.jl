Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
D == midpoint(B, C)
f == internal_angle_bisector(A, B, C)
E == projection(C, f)
g == internal_angle_bisector(B, D, E)
F == line_intersection(g, f)
G == midpoint(E, A)
H == midpoint(D, B)

Need to prove:
collinear(G, F, H)

Proof:
