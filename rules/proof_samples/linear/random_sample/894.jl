Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == external_angle_bisector(C, A, B)
g == internal_angle_bisector(C, A, B)
D == projection(B, g)
c == Circle(D, B, A)
E == center(c)
h == Line(D, E)
F == projection(B, f)
G in h
H == midpoint(F, G)

Need to prove:
collinear(G, E, H)

Proof:
