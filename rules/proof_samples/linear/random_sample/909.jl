Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
F == midpoint(E, D)
h == Line(E, C)
G == midpoint(B, A)
H == projection(B, h)
i == Line(B, H)
I == projection(G, g)
J == projection(I, i)

Need to prove:
collinear(J, F, I)

Proof:
