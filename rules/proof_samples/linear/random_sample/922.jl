Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
j == Line(C, A)
F == projection(D, j)
c == Circle(C, A, G)
H == center(c)
I == midpoint(B, F)

Need to prove:
collinear(H, I, E)

Proof:
