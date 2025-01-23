Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
B in k # (defining k)
H == projection(G, k)

Need to prove:
concyclic(B, D, F, H)

Proof:
