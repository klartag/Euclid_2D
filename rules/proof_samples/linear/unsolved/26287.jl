Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(A, B)
g == internal_angle_bisector(B, A, C)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(g, h)
E in f
c == Circle(B, D, E)
F == projection(E, g)
j == Line(E, F)
G == line_intersection(i, j)

Need to prove:
G in c

Proof:
