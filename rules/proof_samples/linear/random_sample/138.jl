Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, C)
c == Circle(C, A, B)
g == internal_angle_bisector(A, B, C)
h == external_angle_bisector(A, B, C)
D == center(c)
E in h, c
i == Line(E, A)
j == internal_angle_bisector(C, D, A)
F == line_intersection(j, f)
G == line_intersection(i, g)

Need to prove:
concyclic(B, E, F, G)

Proof:
