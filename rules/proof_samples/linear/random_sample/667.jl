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
E == line_intersection(g, i)
F == midpoint(B, D)
d == Circle(F, D, C)
j == external_angle_bisector(B, F, C)
G == center(d)
H in j, d

Need to prove:
collinear(E, H, G)

Proof:
