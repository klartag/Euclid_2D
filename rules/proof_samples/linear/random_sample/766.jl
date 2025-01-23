Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
A in h # (defining h)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E in g
F == projection(D, f)
j == external_angle_bisector(E, B, F)
G == line_intersection(j, h)

Need to prove:
concyclic(B, C, D, G)

Proof:
