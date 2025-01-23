Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
f == external_angle_bisector(A, B, C)
D == midpoint(C, A)
g == parallel_line(D, f)
E == projection(A, f)
c == Circle(D, E, B)
F in g, c

Need to prove:
collinear(F, A, B)

Proof:
