Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
D == midpoint(B, C)
E == midpoint(D, B)
c == Circle(C, E, A)
f == internal_angle_bisector(A, E, B)
d == Circle(A, C, D)
F == center(c)
G == center(d)
H in f, c

Need to prove:
collinear(H, G, F)

Proof:
