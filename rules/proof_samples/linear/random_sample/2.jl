Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
D == midpoint(C, A)
f == internal_angle_bisector(A, C, B)
g == external_angle_bisector(D, B, C)
h == external_angle_bisector(A, C, B)
E == line_intersection(g, f)
c == Circle(C, D, E)
F in h, c
G == center(c)

Need to prove:
collinear(B, G, F)

Proof:
