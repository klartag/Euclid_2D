Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == internal_angle_bisector(A, C, B)
D in f
h == external_angle_bisector(A, B, C)
E == projection(D, h)
c == Circle(A, D, E)
F == line_intersection(h, g)
d == Circle(F, A, C)
G in c, d

Need to prove:
collinear(C, G, E)

Proof:
