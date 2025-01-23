Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
h == parallel_line(A, f)
c == Circle(C, A, B)
i == external_angle_bisector(A, C, B)
D == line_intersection(h, i)
j == internal_angle_bisector(C, A, D)
k == parallel_line(D, g)
E == line_intersection(j, k)
F in h, c

Need to prove:
concyclic(B, D, E, F)

Proof:
