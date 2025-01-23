Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == external_angle_bisector(A, C, B)
g == external_angle_bisector(C, A, B)
D == midpoint(B, A)
E == line_intersection(f, g)
c == Circle(B, E, D)
F in f, c
G == projection(F, g)

Need to prove:
collinear(F, G, D)

Proof:
