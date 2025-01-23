Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(A, B)
g == external_angle_bisector(D, C, A)
E == line_intersection(f, g)
d == Circle(E, D, C)
h == internal_angle_bisector(B, E, D)
F == center(d)
G in h, d

Need to prove:
collinear(B, G, F)

Proof:
