Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D in h
c == Circle(C, D, B)
E == center(c)
j == Line(E, B)
F == line_intersection(i, j)
d == Circle(F, D, E)
G in c, d

Need to prove:
concyclic(A, B, F, G)

Proof:
