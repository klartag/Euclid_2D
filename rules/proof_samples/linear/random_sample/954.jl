Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(C, A)
d == Circle(D, C, E)
F == midpoint(D, B)
e == Circle(F, B, E)
G == center(d)
H == center(e)
I == center(c)

Need to prove:
collinear(G, H, I)

Proof:
