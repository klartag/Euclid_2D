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
c == Circle(A, B, D)
E == center(c)
j == parallel_line(E, h)
F == midpoint(D, C)
G == projection(F, j)
H == projection(D, f)

Need to prove:
concyclic(B, E, G, H)

Proof:
