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
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == line_intersection(g, i)
d == Circle(A, E, B)
G == center(d)
H == projection(F, f)
I == midpoint(E, F)

Need to prove:
collinear(H, I, G)

Proof:
