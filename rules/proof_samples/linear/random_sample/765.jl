Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
d == Circle(C, D, B)
j == internal_angle_bisector(D, A, C)
E == line_intersection(g, i)
F in j, d
G == midpoint(D, C)

Need to prove:
collinear(F, E, G)

Proof:
