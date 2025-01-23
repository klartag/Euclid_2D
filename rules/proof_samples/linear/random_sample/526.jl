Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == external_angle_bisector(A, B, C)
D == midpoint(C, A)
g == internal_angle_bisector(A, C, B)
E == midpoint(D, C)
h == internal_angle_bisector(E, A, B)
F == line_intersection(h, f)
G == line_intersection(g, h)

Need to prove:
concyclic(B, C, F, G)

Proof:
