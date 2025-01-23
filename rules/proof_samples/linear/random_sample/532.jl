Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(B, F)
H == midpoint(C, A)
c == Circle(D, H, A)
I in f, c
J == midpoint(G, I)

Need to prove:
collinear(J, H, I)

Proof:
