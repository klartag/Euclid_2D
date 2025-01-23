Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E in h, c
F == projection(A, h)
G == midpoint(E, C)
d == Circle(F, A, B)

Need to prove:
G in d

Proof:
