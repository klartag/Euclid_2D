Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == center(c)
i == parallel_line(D, g)
d == Circle(E, A, D)
F in i, d

Need to prove:
collinear(E, C, F)

Proof:
