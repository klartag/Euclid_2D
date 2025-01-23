Assumptions:
A, B, C, D, E: Point
f, g, h, i: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i)
f == Line(C, A)
D in f
g == external_angle_bisector(B, D, C)
E == midpoint(C, A)
h == internal_angle_bisector(D, E, B)
i == external_angle_bisector(E, B, D)

Need to prove:
concurrent(g, h, i)

Proof:
