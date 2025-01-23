Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == internal_angle_bisector(A, B, C)
g == external_angle_bisector(A, B, C)
D == projection(A, g)
h == Line(D, A)
E == projection(C, h)
i == Line(E, C)
F == projection(C, f)

Need to prove:
F in i

Proof:
