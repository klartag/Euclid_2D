Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == external_angle_bisector(C, A, B)
c == Circle(C, A, B)
D == center(c)
E in f, c
F == midpoint(E, C)
G == midpoint(C, D)
d == Circle(F, G, C)
H in c, d

Need to prove:
collinear(B, H, F)

Proof:
