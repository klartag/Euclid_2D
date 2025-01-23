Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(C, A)
c == Circle(C, A, B)
D == midpoint(B, C)
E == center(c)
g == external_angle_bisector(A, E, C)
h == parallel_line(D, f)
i == parallel_line(B, g)
F in i, c
j == internal_angle_bisector(C, E, F)
G == line_intersection(j, h)

Need to prove:
concyclic(C, D, E, G)

Proof:
