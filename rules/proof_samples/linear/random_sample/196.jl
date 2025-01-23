Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(D, C)
j == internal_angle_bisector(A, E, B)
F == line_intersection(g, i)
G == line_intersection(j, f)
d == Circle(F, D, E)
H in d, c

Need to prove:
concyclic(B, E, G, H)

Proof:
