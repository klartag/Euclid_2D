Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == center(c)
j == internal_angle_bisector(D, E, C)
k == parallel_line(F, j)

Need to prove:
concurrent(g, i, k)

Proof:
