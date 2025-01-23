Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
d == Circle(D, A, E)
F == line_intersection(g, i)
G == projection(F, f)
j == Line(F, G)
H in j, d

Need to prove:
collinear(B, H, D)

Proof:
