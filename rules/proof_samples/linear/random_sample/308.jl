Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(C, A)
g == internal_angle_bisector(A, B, C)
D in f
h == external_angle_bisector(D, A, B)
E == line_intersection(h, g)
c == Circle(C, E, B)
F == center(c)

Need to prove:
collinear(A, F, E)

Proof:
