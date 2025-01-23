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
E == center(c)
d == Circle(C, E, B)
h == internal_angle_bisector(B, E, A)
F in h, d
G == midpoint(D, B)

Need to prove:
collinear(G, D, F)

Proof:
