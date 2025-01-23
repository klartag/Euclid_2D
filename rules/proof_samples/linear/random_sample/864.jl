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
E == midpoint(C, A)
F == line_intersection(g, i)
j == internal_angle_bisector(B, F, A)
k == parallel_line(E, i)

Need to prove:
concurrent(h, j, k)

Proof:
