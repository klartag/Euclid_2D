Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D in i
c == Circle(C, A, B)
E in h, c
j == internal_angle_bisector(D, A, E)
F == projection(C, j)

Need to prove:
F in h

Proof:
