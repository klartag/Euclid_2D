Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e)
A in c
B in c
C in c
D in c
f == Line(C, A)
g == Line(D, B)
E == line_intersection(f, g)
d == Circle(B, C, E)
e == Circle(A, E, D)
F == center(c)
G == center(e)
H == center(d)
I == midpoint(G, H)

Need to prove:
collinear(F, E, I)

Proof:
