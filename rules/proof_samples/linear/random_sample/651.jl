Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == center(c)
d == Circle(E, A, D)
e == Circle(D, E, B)
i == Line(B, D)
F in g, e
G in i, d
H == projection(G, f)
I == midpoint(H, G)

Need to prove:
collinear(F, G, I)

Proof:
