Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, C, B)
D in h
E == projection(D, f)
F == projection(D, g)
G == projection(E, i)
H == midpoint(F, G)

Need to prove:
collinear(E, F, H)

Proof:
