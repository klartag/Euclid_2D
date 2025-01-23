Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e, h: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e, h)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(A, C, D)
g == external_angle_bisector(A, B, C)
E in g, c
e == Circle(B, E, D)
F == projection(D, f)
h == Circle(F, A, E)
G == line_intersection(g, f)
H in e, h
I in e, d

Need to prove:
concyclic(A, G, H, I)

Proof:
