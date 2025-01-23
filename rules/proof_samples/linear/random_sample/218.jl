Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(D, A)
F == midpoint(B, C)
d == Circle(E, F, B)
G == center(c)
H == center(d)
I == midpoint(E, F)

Need to prove:
collinear(H, G, I)

Proof:
