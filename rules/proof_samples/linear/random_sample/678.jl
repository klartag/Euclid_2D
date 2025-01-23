Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
F == midpoint(C, A)
G == midpoint(D, B)
H == projection(E, h)

Need to prove:
collinear(F, H, G)

Proof:
