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
E == midpoint(B, D)
j == Line(B, D)
F == projection(C, f)
c == Circle(F, A, E)
G in j, c

Need to prove:
concyclic(A, C, D, G)

Proof:
