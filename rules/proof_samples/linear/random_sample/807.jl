Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E == projection(C, i)
d == Circle(E, A, C)
F == center(d)
e == Circle(F, A, B)
G in c, d
H in e, d

Need to prove:
collinear(G, H, B)

Proof:
