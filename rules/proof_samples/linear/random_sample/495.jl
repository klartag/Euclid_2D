Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
A in c
B in c
C in c
f == external_angle_bisector(C, B, A)
g == parallel_line(A, f)
D == projection(B, g)
h == Line(D, B)
E == midpoint(C, A)
F in h, c
G == center(c)

Need to prove:
collinear(F, G, E)

Proof:
