Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == internal_angle_bisector(B, C, D)
k == internal_angle_bisector(C, D, A)
d == Circle(C, D, B)
E == line_intersection(j, k)
F == center(d)
l == Line(E, F)

Need to prove:
concurrent(g, i, l)

Proof:
