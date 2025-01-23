Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(D, C, A)
E == midpoint(D, B)
F == projection(A, h)
G in h, c

Need to prove:
concyclic(B, E, F, G)

Proof:
