Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
D == projection(A, f)
g == internal_angle_bisector(C, D, A)
E == midpoint(B, C)
F == projection(B, g)
h == Line(B, F)
G == projection(C, h)

Need to prove:
concyclic(D, E, F, G)

Proof:
