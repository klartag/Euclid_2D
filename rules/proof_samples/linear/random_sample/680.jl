Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
D == midpoint(B, A)
c == Circle(B, D, C)
E == center(c)
f == internal_angle_bisector(E, B, D)
g == internal_angle_bisector(A, D, E)
F == line_intersection(g, f)

Need to prove:
concyclic(B, C, D, F)

Proof:
