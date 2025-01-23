Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(C, A)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == projection(D, f)
F == projection(A, i)
G == midpoint(C, A)
H == midpoint(A, D)

Need to prove:
concyclic(E, F, G, H)

Proof:
