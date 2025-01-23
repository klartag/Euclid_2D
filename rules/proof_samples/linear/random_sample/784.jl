Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == internal_angle_bisector(A, B, C)
D == midpoint(C, A)
h == internal_angle_bisector(B, C, D)
E == projection(C, g)
F == line_intersection(h, g)
c == Circle(E, F, C)
G in f
d == Circle(G, A, F)
H in c, d

Need to prove:
collinear(H, E, G)

Proof:
