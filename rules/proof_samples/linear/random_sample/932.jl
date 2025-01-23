Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == external_angle_bisector(A, B, C)
h == parallel_line(C, g)
D == midpoint(B, C)
i == parallel_line(C, f)
c == Circle(D, C, A)
E in h, c
F == center(c)
G in i, c
H == midpoint(D, G)

Need to prove:
collinear(H, F, E)

Proof:
