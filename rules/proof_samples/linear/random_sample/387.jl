Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == external_angle_bisector(D, B, C)
E in j, c
d == Circle(D, C, A)
F == center(d)
k == Line(F, E)

Need to prove:
concurrent(g, i, k)

Proof:
