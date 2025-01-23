Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(C, A)
D == midpoint(C, A)
E == midpoint(B, C)
g == internal_angle_bisector(A, D, B)
F == projection(B, g)
h == parallel_line(F, f)

Need to prove:
E in h

Proof:
