Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
c == Circle(C, A, B)
f == external_angle_bisector(C, A, B)
D == center(c)
E == midpoint(D, B)
F in f, c
G == midpoint(F, C)
H == midpoint(G, E)

Need to prove:
collinear(D, F, H)

Proof:
