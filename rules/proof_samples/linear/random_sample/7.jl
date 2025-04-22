Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(A, B)
g == Line(B, C)
h == Line(A, C)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(A, D)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(B, D, G)
d == Circle(A, E, F)
H in d, c

Need to prove:
false()

Proof:
