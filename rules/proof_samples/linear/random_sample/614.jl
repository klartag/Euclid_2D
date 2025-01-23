Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e, h: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e, h)
f == Line(C, A)
c == Circle(C, A, B)
D == midpoint(B, A)
E == center(c)
d == Circle(E, C, A)
g == internal_angle_bisector(B, E, A)
F in f
G in g, d
e == Circle(D, A, F)
h == Circle(B, G, D)
H in e, h

Need to prove:
concyclic(C, F, G, H)

Proof:
