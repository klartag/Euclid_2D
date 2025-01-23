Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
D == projection(A, f)
c == Circle(A, C, D)
h == external_angle_bisector(D, B, A)
E in g, c
F == center(c)
G == projection(C, h)

Need to prove:
collinear(G, E, F)

Proof:
