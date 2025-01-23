Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
d == Circle(B, D, A)
e == Circle(A, E, D)
F == center(d)
h == internal_angle_bisector(B, E, A)
G in h, e

Need to prove:
concyclic(B, C, E, G)

Proof:
