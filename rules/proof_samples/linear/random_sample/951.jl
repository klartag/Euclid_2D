Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == internal_angle_bisector(C, A, B)
g == internal_angle_bisector(A, B, C)
D == line_intersection(f, g)
c == Circle(D, B, A)
E == center(c)
F == midpoint(E, C)
G == midpoint(D, E)

Need to prove:
collinear(C, G, F)

Proof:
