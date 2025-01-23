Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(D, E)
j == Line(D, E)
c == Circle(G, F, C)
d == Circle(D, B, A)
H == center(d)
I in j, c

Need to prove:
collinear(B, I, H)

Proof:
