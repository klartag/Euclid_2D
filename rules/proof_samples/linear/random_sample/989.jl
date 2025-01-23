Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(D, B, A)
g == internal_angle_bisector(C, D, A)
E == midpoint(C, A)
F == midpoint(B, C)
G in f, d
H in g, d

Need to prove:
concyclic(E, F, G, H)

Proof:
