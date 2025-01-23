Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
j == external_angle_bisector(A, E, B)
F == line_intersection(j, g)
G == line_intersection(i, j)

Need to prove:
concyclic(A, B, F, G)

Proof:
