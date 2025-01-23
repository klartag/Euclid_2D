Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
d == Circle(A, E, B)
F == line_intersection(g, i)
G == center(d)
e == Circle(G, F, A)
H in d, e
I == midpoint(C, H)
J == midpoint(B, F)

Need to prove:
collinear(I, F, J)

Proof:
