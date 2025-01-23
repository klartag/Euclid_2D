Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(D, A, C)
c == Circle(A, B, D)
E in j, c
k == internal_angle_bisector(A, C, B)
F == projection(A, k)
G == midpoint(B, D)

Need to prove:
concyclic(B, E, F, G)

Proof:
