Assumptions:
A, B, C, D, E: Point
f, g, h: Line
distinct(A, B, C, D, E)
distinct(f, g, h)
f == internal_angle_bisector(A, B, C)
g == external_angle_bisector(C, A, B)
h == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == line_intersection(f, h)

Need to prove:
concyclic(A, B, D, E)

Proof:
