Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(C, E, B)
H == midpoint(D, G)
d == Circle(G, H, F)
I in c, d

Need to prove:
collinear(C, I, H)

Proof:
