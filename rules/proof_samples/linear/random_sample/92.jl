Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(A, C, B)
d == Circle(E, C, D)
F == center(d)
G in h, d
H in h, c

Need to prove:
concyclic(D, F, G, H)

Proof:
