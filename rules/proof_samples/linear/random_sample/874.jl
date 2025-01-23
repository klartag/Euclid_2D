Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == external_angle_bisector(C, A, B)
g == internal_angle_bisector(A, B, C)
D == projection(C, f)
E == projection(C, g)
F == midpoint(C, A)
G == midpoint(D, E)

Need to prove:
collinear(D, F, G)

Proof:
