Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E == projection(A, g)
d == Circle(E, B, D)
e == Circle(E, A, C)
F in c, e
G in e, d
j == Line(D, F)

Need to prove:
G in j

Proof:
