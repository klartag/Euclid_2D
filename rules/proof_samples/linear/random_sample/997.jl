Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e, h: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e, h)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
F == midpoint(B, A)
d == Circle(F, C, D)
G == center(d)
e == Circle(B, F, D)
h == Circle(B, E, G)
H in h, c
I == center(e)

Need to prove:
concyclic(D, G, H, I)

Proof:
