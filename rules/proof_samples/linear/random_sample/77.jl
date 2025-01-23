Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
c == Circle(A, B, D)
F == center(c)
d == Circle(C, E, F)
G in g, d
H == midpoint(A, D)

Need to prove:
concyclic(A, B, G, H)

Proof:
