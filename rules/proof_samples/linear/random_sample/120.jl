Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
c == Circle(C, B, E)
d == Circle(E, A, D)
F in c, d
j == internal_angle_bisector(C, F, E)

Need to prove:
concurrent(g, h, j)

Proof:
