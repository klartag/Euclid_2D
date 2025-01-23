Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == external_angle_bisector(A, B, C)
g == internal_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in g, c
E == projection(A, g)
F == line_intersection(f, g)
G == midpoint(F, A)

Need to prove:
concyclic(A, D, E, G)

Proof:
