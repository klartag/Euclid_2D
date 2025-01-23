Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(B, C)
c == Circle(C, A, B)
D == center(c)
g == internal_angle_bisector(C, D, A)
E == line_intersection(f, g)
h == external_angle_bisector(B, A, E)
F in h, c

Need to prove:
F in g

Proof:
