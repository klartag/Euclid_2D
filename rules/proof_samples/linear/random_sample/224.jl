Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
A in c
B in c
C in c
f == Line(B, C)
g == Line(C, A)
h == parallel_line(B, g)
D in h, c
i == external_angle_bisector(C, D, A)
j == Line(A, D)
E == center(c)
F in i, c
k == Line(E, F)

Need to prove:
concurrent(f, j, k)

Proof:
