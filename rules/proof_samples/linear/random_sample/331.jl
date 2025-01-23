Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(F, C, D)
H == midpoint(F, B)
I == midpoint(D, G)
d == Circle(G, A, B)
J in c, d

Need to prove:
concyclic(E, H, I, J)

Proof:
