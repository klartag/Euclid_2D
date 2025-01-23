Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == projection(A, g)
F == midpoint(D, B)
h == Line(D, B)
i == parallel_line(A, h)
G in i, c
j == internal_angle_bisector(G, A, F)
H == line_intersection(h, j)

Need to prove:
concyclic(A, E, G, H)

Proof:
