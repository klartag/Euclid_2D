Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(A, D, C)
i == external_angle_bisector(B, C, D)
E in h, c
F == projection(E, i)

Need to prove:
collinear(E, B, F)

Proof:
