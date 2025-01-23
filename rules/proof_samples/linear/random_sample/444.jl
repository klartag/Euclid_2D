Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H, I, J, K)
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
I == midpoint(E, C)
J == midpoint(C, A)
K == midpoint(H, A)

Need to prove:
concyclic(F, I, J, K)

Proof:
