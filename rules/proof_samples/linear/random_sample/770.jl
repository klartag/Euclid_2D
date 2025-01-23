Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
D == midpoint(C, A)
E == midpoint(B, A)
g == external_angle_bisector(E, D, C)
F == line_intersection(f, g)
c == Circle(D, E, F)
G == center(c)
H == projection(C, g)
h == Line(C, H)

Need to prove:
G in h

Proof:
