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
D == line_intersection(h, i)
j == Line(C, A)
c == Circle(A, B, D)
E == projection(B, h)
F in j, c
d == Circle(B, D, E)
G in f, d

Need to prove:
concyclic(A, E, F, G)

Proof:
