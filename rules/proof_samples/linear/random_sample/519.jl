Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(B, A)
g == external_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in g, c
E in f
h == external_angle_bisector(A, D, C)
i == external_angle_bisector(E, B, C)
F == projection(A, h)
j == Line(A, F)

Need to prove:
concurrent(g, i, j)

Proof:
