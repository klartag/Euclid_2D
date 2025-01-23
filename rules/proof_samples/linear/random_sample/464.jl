Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(C, A, D)
E in h, c
d == Circle(B, E, D)
F == center(d)
G == midpoint(B, A)

Need to prove:
collinear(G, E, F)

Proof:
