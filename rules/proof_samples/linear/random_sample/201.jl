Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(A, C, B)
E == midpoint(C, A)
i == internal_angle_bisector(E, A, D)
F == line_intersection(h, i)

Need to prove:
concyclic(B, C, D, F)

Proof:
