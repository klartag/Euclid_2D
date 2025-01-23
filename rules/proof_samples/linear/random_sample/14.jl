Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
f == Line(C, A)
D == midpoint(C, A)
g == internal_angle_bisector(C, B, A)
E == line_intersection(g, f)
F == center(c)
G in g, c
d == Circle(D, B, E)
H in d, c

Need to prove:
collinear(H, G, F)

Proof:
