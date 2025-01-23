Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, C)
D == midpoint(B, C)
c == Circle(C, D, A)
g == Line(D, A)
E == projection(A, f)
h == Line(A, E)
F == center(c)
i == parallel_line(F, h)
G == line_intersection(g, i)

Need to prove:
concyclic(A, C, F, G)

Proof:
