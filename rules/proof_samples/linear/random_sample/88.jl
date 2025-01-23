Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
i == internal_angle_bisector(D, B, C)
E in i, c
j == internal_angle_bisector(A, E, B)
F == line_intersection(h, j)
G == center(c)

Need to prove:
concyclic(B, D, F, G)

Proof:
