Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == center(c)
d == Circle(F, E, C)
e == Circle(A, E, B)
G in h, d
j == Line(B, D)
H in j, e

Need to prove:
concyclic(A, D, G, H)

Proof:
