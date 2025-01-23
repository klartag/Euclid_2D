Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(C, A)
g == external_angle_bisector(A, B, C)
h == parallel_line(B, f)
D == projection(A, h)
E == midpoint(D, C)
c == Circle(C, A, B)
F in g, c
G == center(c)

Need to prove:
collinear(F, E, G)

Proof:
