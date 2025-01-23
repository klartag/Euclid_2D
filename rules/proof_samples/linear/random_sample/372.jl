Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(C, A, D)
E in h, c
F == projection(E, f)
i == Line(E, F)
j == internal_angle_bisector(D, B, E)
k == internal_angle_bisector(C, A, E)

Need to prove:
concurrent(i, j, k)

Proof:
