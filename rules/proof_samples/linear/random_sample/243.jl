Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
D == midpoint(C, A)
E == projection(B, g)
h == Line(E, B)
F == projection(D, h)
i == external_angle_bisector(A, B, C)
G == projection(C, i)

Need to prove:
collinear(D, F, G)

Proof:
