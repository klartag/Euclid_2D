Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E in i, c
F == midpoint(E, A)
G == midpoint(E, F)
d == Circle(F, E, C)
H == center(d)
I == midpoint(E, B)

Need to prove:
collinear(G, I, H)

Proof:
