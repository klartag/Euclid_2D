Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(A, C, B)
i == external_angle_bisector(A, B, C)
D == line_intersection(i, g)
c == Circle(A, B, D)
E in f, c
F == center(c)
j == internal_angle_bisector(D, E, C)
G == line_intersection(j, h)

Need to prove:
collinear(G, F, D)

Proof:
