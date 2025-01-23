Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == external_angle_bisector(C, A, B)
D == projection(C, f)
c == Circle(D, C, A)
d == Circle(C, D, B)
E in h, d
F == center(c)
j == parallel_line(C, g)
k == Line(E, F)

Need to prove:
concurrent(i, j, k)

Proof:
