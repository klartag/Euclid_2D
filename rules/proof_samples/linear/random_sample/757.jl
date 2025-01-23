Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E == midpoint(B, D)
j == Line(B, D)
F == center(c)
G == projection(C, j)
H == midpoint(G, A)

Need to prove:
collinear(F, H, E)

Proof:
