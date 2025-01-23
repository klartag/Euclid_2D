Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, A, B)
j == Line(C, A)
d == Circle(A, B, D)
E in h, d
F in j, d
e == Circle(C, F, E)
G in e, c
k == Line(E, G)

Need to prove:
concurrent(f, j, k)

Proof:
