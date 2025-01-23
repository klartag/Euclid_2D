Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, C)
c == Circle(C, A, B)
D == midpoint(C, A)
g == internal_angle_bisector(D, A, B)
E == line_intersection(f, g)
F == projection(C, g)
G == center(c)
d == Circle(F, D, G)
H in g, d

Need to prove:
concyclic(C, E, G, H)

Proof:
