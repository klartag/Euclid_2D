Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, C)
E == center(c)
F == midpoint(B, A)
d == Circle(B, F, E)
G == center(d)
f == Line(E, D)
g == internal_angle_bisector(D, G, F)
H == line_intersection(f, g)

Need to prove:
concyclic(E, F, G, H)

Proof:
