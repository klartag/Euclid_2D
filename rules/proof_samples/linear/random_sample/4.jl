Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == external_angle_bisector(C, A, B)
g == internal_angle_bisector(A, C, B)
c == Circle(C, A, B)
h == internal_angle_bisector(A, B, C)
D == line_intersection(f, g)
E == midpoint(D, C)
F in f, c
G == line_intersection(h, g)

Need to prove:
concyclic(A, E, F, G)

Proof:
