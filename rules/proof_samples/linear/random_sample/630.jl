Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(A, D)
j == external_angle_bisector(E, D, B)
F == line_intersection(g, i)
k == internal_angle_bisector(E, A, C)
l == internal_angle_bisector(B, F, A)

Need to prove:
concurrent(j, k, l)

Proof:
