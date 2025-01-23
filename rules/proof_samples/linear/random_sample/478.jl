Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, A)
f == external_angle_bisector(C, A, B)
E in f, c
d == Circle(C, D, A)
g == Line(E, D)
F == center(c)
G in g, d

Need to prove:
concyclic(C, E, F, G)

Proof:
