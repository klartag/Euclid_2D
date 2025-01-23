Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
g == internal_angle_bisector(A, B, C)
h == parallel_line(A, g)
D == line_intersection(f, h)
E == midpoint(D, A)
F == midpoint(B, C)
c == Circle(E, D, B)
d == Circle(E, F, B)
G in h, d
H == center(c)
I == midpoint(D, G)

Need to prove:
concyclic(E, F, H, I)

Proof:
