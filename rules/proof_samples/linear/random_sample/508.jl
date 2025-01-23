Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(A, D)
j == external_angle_bisector(C, B, E)
F == projection(C, j)
c == Circle(F, B, C)
G == center(c)

Need to prove:
collinear(D, G, F)

Proof:
