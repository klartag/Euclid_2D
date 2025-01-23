Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == midpoint(D, C)
i == Line(B, D)
j == parallel_line(E, g)
F == line_intersection(i, j)
G == midpoint(C, A)

Need to prove:
concyclic(A, B, F, G)

Proof:
