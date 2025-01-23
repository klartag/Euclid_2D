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
h == Line(C, A)
i == internal_angle_bisector(B, D, A)
E in i, c
F == center(c)
j == Line(E, F)
k == Line(D, B)

Need to prove:
concurrent(h, j, k)

Proof:
