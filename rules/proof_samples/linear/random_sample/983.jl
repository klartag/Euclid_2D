Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == center(c)
d == Circle(C, A, E)
i == external_angle_bisector(D, B, C)
F in i, c
G in g, d

Need to prove:
collinear(G, F, E)

Proof:
