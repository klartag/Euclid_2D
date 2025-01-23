Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
c == Circle(C, A, B)
g == internal_angle_bisector(A, C, B)
D == center(c)
E in g, c
F == projection(E, f)
h == parallel_line(C, f)
G == projection(D, h)
H == midpoint(F, D)

Need to prove:
collinear(E, G, H)

Proof:
