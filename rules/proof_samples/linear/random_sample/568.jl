Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(D, C)
j == Line(E, A)
F == line_intersection(j, g)
c == Circle(F, A, B)
G == center(c)

Need to prove:
concyclic(C, E, F, G)

Proof:
