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
h == external_angle_bisector(B, D, C)
E == projection(B, h)
F == midpoint(C, A)
G in h, c

Need to prove:
concyclic(A, E, F, G)

Proof:
