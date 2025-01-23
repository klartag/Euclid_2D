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
i == external_angle_bisector(A, C, B)
j == internal_angle_bisector(D, B, C)
E == center(c)
d == Circle(B, D, E)
F in g, d
k == Line(F, E)

Need to prove:
concurrent(i, j, k)

Proof:
