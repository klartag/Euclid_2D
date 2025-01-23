Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, C)
g == external_angle_bisector(A, C, B)
h == internal_angle_bisector(A, C, B)
D == projection(B, h)
i == Line(D, A)
c == Circle(B, D, A)
E in f, c
F == line_intersection(i, g)
G == center(c)
H == midpoint(B, C)

Need to prove:
concyclic(E, F, G, H)

Proof:
