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
H == midpoint(F, D)
I == projection(H, f)
J == midpoint(D, G)

Need to prove:
collinear(J, I, H)

Proof:
