Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
E == projection(B, h)
F == midpoint(C, A)
j == Line(C, A)
d == Circle(E, B, D)
e == Circle(B, E, F)
G in j, e
H in c, d

Need to prove:
collinear(E, H, G)

Proof:
