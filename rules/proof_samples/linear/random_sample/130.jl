Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
h == internal_angle_bisector(E, D, B)
d == Circle(D, C, E)
F == center(d)
i == internal_angle_bisector(E, C, A)
j == internal_angle_bisector(B, F, A)

Need to prove:
concurrent(h, i, j)

Proof:
