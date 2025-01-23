Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
distinct(c, d)
A in c
B in c
f == Line(A, B)
C == center(c)
g == internal_angle_bisector(A, C, B)
D == line_intersection(f, g)
d == Circle(B, A, C)
E == center(d)
F == midpoint(A, C)

Need to prove:
concyclic(A, D, E, F)

Proof:
