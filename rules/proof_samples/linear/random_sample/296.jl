Assumptions:
A, B, C, D: Point
f, g, h: Line
distinct(A, B, C, D)
distinct(f, g, h)
D == midpoint(B, A)
f == internal_angle_bisector(C, A, D)
g == external_angle_bisector(A, C, B)
h == external_angle_bisector(D, B, C)

Need to prove:
concurrent(f, g, h)

Proof:
