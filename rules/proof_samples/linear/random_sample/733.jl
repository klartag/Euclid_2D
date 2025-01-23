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
D == projection(A, g)
i == Line(D, A)
c == Circle(B, D, A)
E in h, c
d == Circle(D, C, A)
j == Line(E, B)
F in f, d
G == center(d)
H == line_intersection(j, i)
I == midpoint(A, H)

Need to prove:
concyclic(E, F, G, I)

Proof:
