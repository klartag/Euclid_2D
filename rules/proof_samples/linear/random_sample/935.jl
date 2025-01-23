Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == midpoint(B, A)
d == Circle(F, D, C)
G in g, d
e == Circle(G, E, F)
H == center(e)
I == midpoint(H, D)

Need to prove:
collinear(D, I, F)

Proof:
