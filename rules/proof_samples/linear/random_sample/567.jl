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
d == Circle(A, B, D)
E == center(d)
e == Circle(B, D, E)
F == projection(E, i)
j == Line(F, E)
G == line_intersection(h, j)
H in g, e

Need to prove:
concyclic(A, C, G, H)

Proof:
