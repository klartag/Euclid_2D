Assumptions:
A, B, C, D, E: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == internal_angle_bisector(D, B, C)
k == internal_angle_bisector(D, A, C)
E == line_intersection(j, k)
l == internal_angle_bisector(D, E, C)

Need to prove:
concurrent(g, i, l)

Proof:
