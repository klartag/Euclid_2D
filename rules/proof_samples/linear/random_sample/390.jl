Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
j == Line(E, F)
G == line_intersection(i, j)
c == Circle(F, G, B)
d == Circle(A, B, D)
H in d, c

Need to prove:
collinear(F, D, H)

Proof:
