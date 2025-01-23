Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == internal_angle_bisector(A, C, B)
h == internal_angle_bisector(C, A, B)
i == external_angle_bisector(C, A, B)
D in f
j == external_angle_bisector(D, C, A)
E == line_intersection(j, i)
k == Line(E, B)

Need to prove:
concurrent(g, h, k)

Proof:
