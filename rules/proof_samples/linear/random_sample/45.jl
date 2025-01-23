Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
j == parallel_line(E, h)
F == projection(E, f)
G == projection(C, j)
H == midpoint(D, G)

Need to prove:
collinear(E, F, H)

Proof:
