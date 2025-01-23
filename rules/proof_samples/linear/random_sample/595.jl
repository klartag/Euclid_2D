Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(D, B, A)
e == Circle(B, C, D)
E in f, e
g == external_angle_bisector(B, D, E)
F == projection(B, g)
h == Line(B, F)
G in h, c
H == center(d)
I == midpoint(G, E)

Need to prove:
collinear(H, G, I)

Proof:
