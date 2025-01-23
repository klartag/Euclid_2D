Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
h == external_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in h, c
E in g, c
F == midpoint(D, E)
d == Circle(F, C, E)
G == center(d)

Need to prove:
concyclic(C, D, F, G)

Proof:
