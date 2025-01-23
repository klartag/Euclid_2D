Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(B, A)
F == midpoint(E, C)
G == center(c)
d == Circle(G, E, D)
H in c, d

Need to prove:
collinear(C, H, F)

Proof:
