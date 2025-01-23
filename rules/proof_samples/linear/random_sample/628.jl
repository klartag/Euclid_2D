Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
A in c
B in c
C in c
D == midpoint(C, A)
E == midpoint(C, D)
d == Circle(B, E, C)
f == external_angle_bisector(E, A, B)
F == center(c)
G == center(d)
H in f, c

Need to prove:
collinear(G, H, F)

Proof:
