Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d, e)
c == Circle(C, A, B)
f == internal_angle_bisector(A, B, C)
D == center(c)
d == Circle(A, C, D)
E in f, c
e == Circle(D, C, E)
F == center(e)
g == Line(F, D)
G in g, d

Need to prove:
concyclic(C, E, F, G)

Proof:
