Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, C)
c == Circle(C, A, B)
D == center(c)
d == Circle(B, C, D)
E == center(d)
g == parallel_line(A, f)
F == projection(E, f)
G == projection(F, g)

Need to prove:
collinear(D, E, G)

Proof:
