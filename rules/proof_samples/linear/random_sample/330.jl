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
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(B, i)
j == Line(E, B)
c == Circle(A, E, B)
F == line_intersection(j, h)
d == Circle(D, C, A)
G == midpoint(F, D)
H in d, c

Need to prove:
collinear(A, G, H)

Proof:
