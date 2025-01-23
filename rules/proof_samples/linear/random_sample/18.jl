Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
D == projection(A, g)
E == projection(C, f)
c == Circle(C, A, B)
F == midpoint(B, A)
h == parallel_line(F, g)
G == center(c)
i == Line(C, G)
H == line_intersection(i, h)
d == Circle(H, E, D)
I == center(d)

Need to prove:
collinear(D, H, I)

Proof:
