Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == Line(C, A)
D == midpoint(B, A)
c == Circle(C, B, D)
E in f, c
d == Circle(B, E, A)
e == Circle(C, D, A)
F in d, e
g == external_angle_bisector(F, E, D)
G == center(c)
H in g, c

Need to prove:
collinear(H, G, F)

Proof:
