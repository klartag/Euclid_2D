Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
H in k
I == midpoint(G, H)

Need to prove:
collinear(C, H, I)

Proof:
