Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == line_intersection(g, i)
d == Circle(B, D, F)
e == Circle(D, A, E)
G in e, d

Need to prove:
false() # collinear(D, E, G)

Proof:
