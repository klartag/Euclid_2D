Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
k == Line(E, D)
H == midpoint(F, A)
I == midpoint(C, F)
l == Line(I, H)
J == line_intersection(k, l)

Need to prove:
concyclic(D, G, I, J)

Proof:
