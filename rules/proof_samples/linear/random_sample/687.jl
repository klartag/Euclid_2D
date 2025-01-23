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
E == center(c)
F == midpoint(E, C)
G == midpoint(A, E)
d == Circle(E, F, B)
e == Circle(G, F, D)
H in d, c
I in c, e

Need to prove:
collinear(I, H, F)

Proof:
