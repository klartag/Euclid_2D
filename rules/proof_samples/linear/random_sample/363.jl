Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == parallel_line(D, g)
E == center(c)
F == midpoint(C, A)
G in i, c
H == midpoint(G, E)
I == midpoint(H, F)

Need to prove:
collinear(E, C, I)

Proof:
