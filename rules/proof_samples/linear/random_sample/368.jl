Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == external_angle_bisector(A, B, C)
D == projection(A, h)
i == parallel_line(D, f)
c == Circle(D, C, A)
E == center(c)
d == Circle(C, A, B)
F in h, d
j == Line(F, E)

Need to prove:
concurrent(g, i, j)

Proof:
