Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == external_angle_bisector(A, C, B)
g == parallel_line(B, f)
D == projection(C, g)
E == midpoint(C, A)
F == midpoint(E, B)
h == internal_angle_bisector(B, E, A)
G == projection(B, h)

Need to prove:
collinear(F, G, D)

Proof:
