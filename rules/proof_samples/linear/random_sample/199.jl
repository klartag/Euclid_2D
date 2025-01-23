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
c == Circle(C, A, B)
D in i, c
E == center(c)
F in h, c
j == Line(E, B)
d == Circle(F, E, C)
G in j, d

Need to prove:
collinear(D, G, C)

Proof:
