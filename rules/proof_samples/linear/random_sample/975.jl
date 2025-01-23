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
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
c == Circle(C, B, E)
d == Circle(D, E, C)
j == internal_angle_bisector(D, B, C)
F == center(c)
G == center(d)
H in j, c

Need to prove:
collinear(F, H, G)

Proof:
