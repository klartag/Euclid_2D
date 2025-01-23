Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
c == Circle(C, A, B)
F == midpoint(A, D)
d == Circle(C, E, F)
G in i, d
e == Circle(G, D, C)
H in c, e

Need to prove:
collinear(H, E, B)

Proof:
