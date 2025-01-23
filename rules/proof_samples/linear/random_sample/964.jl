Assumptions:
A, B, C, D, E: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E)
distinct(f, g, h, i, j)
A in c
B in c
C in c
f == Line(A, B)
g == Line(B, C)
h == external_angle_bisector(A, C, B)
D in h, c
E == midpoint(C, A)
i == parallel_line(E, g)
j == internal_angle_bisector(B, D, A)

Need to prove:
concurrent(f, i, j)

Proof:
