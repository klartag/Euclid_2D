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
c == Circle(D, C, A)
E == midpoint(D, C)
F in f, c
d == Circle(F, E, C)
G in f, d
H == midpoint(E, G)

Need to prove:
collinear(B, D, H)

Proof:
