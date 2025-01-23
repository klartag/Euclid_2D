Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == Line(B, C)
D in f
E == midpoint(B, A)
F == midpoint(D, A)
g == internal_angle_bisector(F, D, C)
h == external_angle_bisector(D, B, E)
i == internal_angle_bisector(D, A, B)

Need to prove:
concurrent(g, h, i)

Proof:
