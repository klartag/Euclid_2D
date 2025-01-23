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
E == midpoint(B, D)
c == Circle(C, A, B)
F == projection(A, g)
G in i, c
H == midpoint(G, D)
j == Line(H, E)

Need to prove:
F in j

Proof:
