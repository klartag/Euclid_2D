Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D == projection(B, g)
h == Line(D, B)
E == center(c)
i == Line(E, A)
F in h, c
G in i
H == midpoint(G, E)

Need to prove:
collinear(F, H, G)

Proof:
