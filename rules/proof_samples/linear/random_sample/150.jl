Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == Line(C, A)
c == Circle(C, A, B)
D == midpoint(C, A)
g == internal_angle_bisector(D, B, A)
E in g, c
F == line_intersection(f, g)
d == Circle(A, F, B)
G == center(d)
e == Circle(E, G, D)
H in e, c

Need to prove:
concyclic(A, F, G, H)

Proof:
