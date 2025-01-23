Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
h == parallel_line(B, g)
c == Circle(C, A, B)
D == midpoint(C, A)
E == center(c)
d == Circle(E, A, D)
F in f, d
i == parallel_line(F, h)
G == midpoint(B, D)

Need to prove:
G in i

Proof:
