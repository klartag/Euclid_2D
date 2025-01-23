Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(C, A)
g == internal_angle_bisector(C, A, B)
h == parallel_line(B, g)
c == Circle(C, A, B)
D in h, c
i == parallel_line(D, f)
E == center(c)
F in i, c
j == internal_angle_bisector(A, E, F)
G == midpoint(D, C)
H == line_intersection(g, j)

Need to prove:
concyclic(D, F, G, H)

Proof:
