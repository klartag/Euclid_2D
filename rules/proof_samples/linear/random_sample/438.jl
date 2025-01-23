Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(A, g)
c == Circle(C, A, B)
D == center(c)
E == projection(D, h)
i == Line(D, E)
F in f
G == midpoint(B, F)
d == Circle(D, C, A)
H in i, d

Need to prove:
collinear(F, G, H)

Proof:
