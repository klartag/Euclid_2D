Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
D == midpoint(C, A)
f == internal_angle_bisector(D, B, A)
g == external_angle_bisector(B, D, C)
E == line_intersection(g, f)
c == Circle(E, B, D)
F == center(c)

Need to prove:
concyclic(A, B, D, F)

Proof:
