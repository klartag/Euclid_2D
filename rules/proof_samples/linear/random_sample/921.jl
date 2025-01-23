Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == parallel_line(A, f)
c == Circle(C, A, B)
D == midpoint(B, A)
i == parallel_line(D, h)
E == line_intersection(g, i)
F == center(c)
d == Circle(C, F, A)
G == center(d)

Need to prove:
collinear(F, G, E)

Proof:
