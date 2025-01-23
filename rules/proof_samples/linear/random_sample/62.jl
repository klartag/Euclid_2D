Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
F == midpoint(C, A)
c == Circle(A, F, B)
d == Circle(E, D, F)
G in h, d
H in d, c

Need to prove:
collinear(H, A, G)

Proof:
