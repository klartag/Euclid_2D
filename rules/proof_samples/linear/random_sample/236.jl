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
E == line_intersection(g, i)
j == parallel_line(E, h)
F == midpoint(A, D)
k == internal_angle_bisector(B, F, A)
l == internal_angle_bisector(F, B, C)

Need to prove:
concurrent(j, k, l)

Proof:
