Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
c == Circle(C, A, B)
D == center(c)
h == Line(D, C)
i == parallel_line(D, g)
E == projection(B, i)
j == Line(E, B)
F == line_intersection(h, j)
G == line_intersection(f, i)

Need to prove:
concyclic(A, D, F, G)

Proof:
