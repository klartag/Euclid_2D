Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(C, A)
D == projection(C, f)
h == Line(C, D)
E == midpoint(D, A)
c == Circle(B, C, D)
F == center(c)
i == external_angle_bisector(B, F, D)
G == line_intersection(i, g)
H == line_intersection(h, i)

Need to prove:
concyclic(D, E, G, H)

Proof:
