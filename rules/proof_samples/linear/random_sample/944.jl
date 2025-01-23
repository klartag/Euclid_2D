Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == internal_angle_bisector(C, A, B)
g == external_angle_bisector(A, B, C)
c == Circle(C, A, B)
D in g, c
E == projection(D, f)
F == line_intersection(f, g)
G == midpoint(C, F)

Need to prove:
concyclic(D, E, F, G)

Proof:
