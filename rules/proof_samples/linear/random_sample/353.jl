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
c == Circle(C, D, B)
E in i, c
d == Circle(A, E, B)
F == center(d)
G == midpoint(B, F)
H == midpoint(E, A)

Need to prove:
collinear(F, H, G)

Proof:
