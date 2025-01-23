Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E in i, c
j == internal_angle_bisector(E, B, A)
F == line_intersection(i, j)
G == midpoint(D, E)
H == midpoint(B, C)

Need to prove:
concyclic(B, F, G, H)

Proof:
