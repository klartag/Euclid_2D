Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(G, C)
I == midpoint(G, F)
J == midpoint(H, I)

Need to prove:
collinear(F, J, G)

Proof:
