Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d, e)
A in c
B in c
C in c
D in c
f == Line(A, B)
g == Line(C, D)
h == Line(C, A)
E == center(c)
d == Circle(D, B, E)
F in g, d
e == Circle(F, E, C)
G == center(e)
H == projection(F, f)
i == Line(F, H)
I in h, e
J in i, e

Need to prove:
collinear(J, I, G)

Proof:
