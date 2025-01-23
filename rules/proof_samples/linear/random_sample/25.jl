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
E == center(c)
h == Line(A, E)
F == line_intersection(g, h)
d == Circle(A, F, D)
G == center(d)
H == midpoint(B, G)

Need to prove:
collinear(H, D, G)

Proof:
