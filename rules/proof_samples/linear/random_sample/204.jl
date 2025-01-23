Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == external_angle_bisector(C, A, B)
c == Circle(C, A, B)
h == internal_angle_bisector(C, A, B)
D == center(c)
E in g, c
F in h, c
G == midpoint(D, F)
H == projection(E, f)

Need to prove:
collinear(F, G, H)

Proof:
