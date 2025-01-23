Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
g == external_angle_bisector(C, A, B)
c == Circle(C, A, B)
D == center(c)
h == internal_angle_bisector(B, D, C)
E == projection(C, g)
d == Circle(C, A, E)
F == line_intersection(h, f)
G == center(d)

Need to prove:
collinear(F, E, G)

Proof:
