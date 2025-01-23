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
j == internal_angle_bisector(D, B, C)
E == line_intersection(g, i)
F == midpoint(B, A)
G in j, c
H == midpoint(G, E)

Need to prove:
collinear(G, F, H)

Proof:
