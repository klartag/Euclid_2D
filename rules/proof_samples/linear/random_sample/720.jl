Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
D == midpoint(C, A)
c == Circle(C, A, B)
g == external_angle_bisector(D, C, B)
E == center(c)
F == projection(E, g)
G == line_intersection(f, g)
d == Circle(E, F, B)
H in f, d

Need to prove:
concyclic(D, E, G, H)

Proof:
