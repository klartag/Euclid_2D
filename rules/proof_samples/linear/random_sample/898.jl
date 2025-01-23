Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E in g
F == line_intersection(j, f)
k == internal_angle_bisector(D, F, B)
l == internal_angle_bisector(E, C, D)

Need to prove:
concurrent(i, k, l)

Proof:
