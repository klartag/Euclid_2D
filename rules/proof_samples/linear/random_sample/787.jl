Assumptions:
A, B, C, D, E: Point
f, g, h: Line
distinct(A, B, C, D, E)
distinct(f, g, h)
f == external_angle_bisector(A, C, B)
D == midpoint(B, A)
g == external_angle_bisector(C, B, D)
E == midpoint(C, A)
h == internal_angle_bisector(E, A, B)

Need to prove:
concurrent(f, g, h)

Proof:
