Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == parallel_line(A, f)
D == midpoint(B, A)
E == projection(C, g)
c == Circle(B, C, E)
h == external_angle_bisector(B, E, A)
F == midpoint(E, B)
G in h, c

Need to prove:
collinear(G, D, F)

Proof:
