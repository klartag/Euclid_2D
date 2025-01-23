Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, C)
c == Circle(C, A, B)
g == external_angle_bisector(C, A, B)
D == line_intersection(f, g)
E == center(c)
F == projection(E, g)
d == Circle(A, E, D)
G in f, d

Need to prove:
collinear(G, E, F)

Proof:
