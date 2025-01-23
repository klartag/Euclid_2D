Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
D == midpoint(B, A)
g == external_angle_bisector(C, D, A)
c == Circle(C, B, D)
E in g, c
F == center(c)
G == projection(F, f)
h == Line(F, G)

Need to prove:
E in h

Proof:
