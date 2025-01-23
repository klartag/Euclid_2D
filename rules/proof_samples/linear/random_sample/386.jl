Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(B, C)
g == external_angle_bisector(A, C, B)
h == parallel_line(A, g)
D == line_intersection(f, h)
E == midpoint(B, C)
c == Circle(A, E, D)
F == center(c)

Need to prove:
concyclic(A, C, E, F)

Proof:
