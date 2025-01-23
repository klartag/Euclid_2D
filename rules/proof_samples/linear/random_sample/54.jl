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
j == Line(B, D)
c == Circle(C, D, B)
E == center(c)
d == Circle(C, E, A)
F == midpoint(A, E)
G == center(d)
H == projection(E, j)

Need to prove:
concyclic(A, F, G, H)

Proof:
