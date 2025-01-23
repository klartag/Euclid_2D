Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == internal_angle_bisector(A, C, B)
g == internal_angle_bisector(A, B, C)
D == midpoint(B, A)
c == Circle(C, A, B)
h == internal_angle_bisector(C, A, D)
E in f, c
F == projection(E, h)
i == parallel_line(F, g)

Need to prove:
D in i

Proof:
