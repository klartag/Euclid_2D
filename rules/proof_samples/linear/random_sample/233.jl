Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == internal_angle_bisector(C, A, B)
g == external_angle_bisector(C, A, B)
D == projection(C, g)
E == midpoint(C, D)
F == midpoint(E, A)
G == projection(E, f)

Need to prove:
collinear(D, F, G)

Proof:
