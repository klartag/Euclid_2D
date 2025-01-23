Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == midpoint(B, C)
E == projection(D, h)
c == Circle(D, E, B)
F == midpoint(C, A)
G == projection(F, i)
H in h, c

Need to prove:
collinear(H, D, G)

Proof:
