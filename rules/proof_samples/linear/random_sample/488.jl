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
h == internal_angle_bisector(B, D, C)
i == internal_angle_bisector(D, C, A)
E == midpoint(B, A)
F == line_intersection(h, i)
G == projection(B, i)

Need to prove:
concyclic(B, E, F, G)

Proof:
