Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(D, C, A)
i == external_angle_bisector(B, D, C)
E == midpoint(B, A)
F == line_intersection(h, i)
G == projection(B, h)

Need to prove:
concyclic(B, E, F, G)

Proof:
