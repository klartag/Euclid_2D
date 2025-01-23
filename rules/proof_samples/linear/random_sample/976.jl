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
h == external_angle_bisector(C, A, B)
E == projection(C, h)
i == Line(C, E)
F == line_intersection(i, f)
j == Line(E, B)
G == line_intersection(g, j)

Need to prove:
concyclic(A, D, F, G)

Proof:
