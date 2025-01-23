Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
c == Circle(B, E, A)
d == Circle(D, F, E)
G == center(c)
e == Circle(A, F, B)
H in d, e

Need to prove:
collinear(C, H, G)

Proof:
