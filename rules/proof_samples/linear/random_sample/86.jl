Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E in f
j == external_angle_bisector(A, B, E)
c == Circle(C, D, B)
F in j, c
G == line_intersection(j, i)

Need to prove:
concyclic(A, C, F, G)

Proof:
