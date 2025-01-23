Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d, e)
f == Line(B, C)
g == internal_angle_bisector(A, C, B)
c == Circle(C, A, B)
D == center(c)
d == Circle(D, C, A)
E in g, c
F in f, d
e == Circle(E, A, F)
G == center(e)

Need to prove:
concyclic(A, C, D, G)

Proof:
