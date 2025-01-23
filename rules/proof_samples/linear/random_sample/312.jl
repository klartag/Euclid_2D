Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
c == Circle(C, A, B)
f == internal_angle_bisector(A, B, C)
g == external_angle_bisector(A, B, C)
D in g, c
h == Line(D, A)
E == center(c)
F == line_intersection(h, f)
i == Line(E, D)
G == projection(F, i)

Need to prove:
collinear(C, B, G)

Proof:
