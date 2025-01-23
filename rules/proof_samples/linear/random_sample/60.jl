Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E in f
F == projection(D, g)
c == Circle(F, E, B)
d == Circle(A, B, D)
G in d, c
H == line_intersection(i, g)

Need to prove:
collinear(G, F, H)

Proof:
