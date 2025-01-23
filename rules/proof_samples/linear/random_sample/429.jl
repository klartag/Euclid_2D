Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
h == Line(D, B)
i == internal_angle_bisector(B, E, A)
F == midpoint(C, A)
G == line_intersection(h, i)

Need to prove:
collinear(A, F, G)

Proof:
