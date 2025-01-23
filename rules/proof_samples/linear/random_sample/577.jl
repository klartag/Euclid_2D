Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == line_intersection(g, i)
j == external_angle_bisector(C, E, B)
d == Circle(A, E, F)
G in j, d
H == projection(A, h)

Need to prove:
collinear(A, H, G)

Proof:
