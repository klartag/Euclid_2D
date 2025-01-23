Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(C, A)
c == Circle(C, A, B)
D == center(c)
E == midpoint(D, C)
h == external_angle_bisector(B, C, E)
F in h, c
G == projection(F, g)
i == Line(F, G)
H == line_intersection(f, i)

Need to prove:
concyclic(B, D, F, H)

Proof:
