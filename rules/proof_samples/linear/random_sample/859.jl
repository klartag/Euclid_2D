Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(C, f)
i == Line(D, C)
E == projection(A, g)
j == Line(E, A)
F == line_intersection(i, j)
c == Circle(A, D, F)
G in h, c
d == Circle(D, C, A)
H == center(d)
I == midpoint(B, C)

Need to prove:
concyclic(E, G, H, I)

Proof:
