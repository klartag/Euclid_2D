Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == external_angle_bisector(C, A, B)
D == projection(C, f)
g == Line(D, C)
h == internal_angle_bisector(A, B, C)
E == line_intersection(f, h)
c == Circle(C, E, B)
F in g, c
d == Circle(G, F, C)
H == center(d)

Need to prove:
collinear(H, D, A)

Proof:
