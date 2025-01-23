Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == internal_angle_bisector(A, B, C)
g == external_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in g, c
E == center(c)
h == internal_angle_bisector(C, E, B)
F == projection(D, f)
i == Line(F, D)
G == line_intersection(h, i)

Need to prove:
concyclic(A, B, C, G)

Proof:
