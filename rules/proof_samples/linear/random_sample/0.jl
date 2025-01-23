Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, A)
h == parallel_line(D, g)
c == Circle(A, C, D)
E in h, c
F == midpoint(E, D)
i == internal_angle_bisector(A, F, C)
j == Line(C, E)

Need to prove:
concurrent(f, i, j)

Proof:
