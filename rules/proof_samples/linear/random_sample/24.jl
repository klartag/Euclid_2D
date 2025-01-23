Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(B, C)
g == Line(C, A)
h == Line(D, B)
E == line_intersection(h, g)
F == midpoint(B, C)
d == Circle(A, F, C)
i == Line(E, F)
G in i, d
j == Line(A, D)
H == line_intersection(f, j)
I == center(c)

Need to prove:
concyclic(F, G, H, I)

Proof:
