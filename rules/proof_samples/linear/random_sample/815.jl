Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
G == midpoint(C, A)
i == external_angle_bisector(F, G, A)
H == line_intersection(i, g)

Need to prove:
concyclic(D, E, F, H)

Proof:
