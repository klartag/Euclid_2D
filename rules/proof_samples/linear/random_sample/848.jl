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
h == external_angle_bisector(A, C, B)
i == Line(C, A)
E in h, c
F == projection(E, g)
j == Line(E, F)
k == Line(D, B)

Need to prove:
concurrent(i, j, k)

Proof:
