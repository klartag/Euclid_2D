Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == Line(B, A)
g == internal_angle_bisector(C, A, B)
B in h # (defining h)
D == line_intersection(h, g)
E == projection(D, f)
c == Circle(B, D, A)
i == external_angle_bisector(E, A, C)
F in i, c

Need to prove:
collinear(F, C, D)

Proof:
