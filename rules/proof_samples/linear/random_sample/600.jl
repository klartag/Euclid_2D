Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == external_angle_bisector(A, B, C)
c == Circle(C, A, B)
D == midpoint(C, A)
E == center(c)
d == Circle(B, C, D)
g == Line(E, A)
F == line_intersection(f, g)
G in f, c
e == Circle(A, F, B)
H in e, d

Need to prove:
concyclic(A, D, G, H)

Proof:
