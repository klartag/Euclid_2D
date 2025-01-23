Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
D == projection(A, g)
E == midpoint(C, D)
F == midpoint(D, B)
G == midpoint(B, A)
c == Circle(F, E, G)
H in f, c
d == Circle(H, B, C)
I in d, c

Need to prove:
collinear(A, I, C)

Proof:
