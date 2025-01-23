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
c == Circle(C, A, B)
E in h, c
F == midpoint(D, E)
d == Circle(C, F, A)
G == center(d)
H == projection(C, f)

Need to prove:
collinear(F, H, G)

Proof:
