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
F == midpoint(D, C)
c == Circle(F, A, C)
G == center(c)
j == Line(G, E)
H == line_intersection(j, h)

Need to prove:
concyclic(A, F, G, H)

Proof:
