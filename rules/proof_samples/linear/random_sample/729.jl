Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
D == midpoint(B, C)
E == midpoint(C, A)
c == Circle(A, C, D)
F in f, c
G == projection(F, g)
h == Line(F, G)
H == center(c)
d == Circle(D, H, E)
I in h, c
J in d, c

Need to prove:
collinear(I, H, J)

Proof:
