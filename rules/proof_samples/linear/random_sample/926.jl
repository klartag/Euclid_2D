Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(C, F)
H == midpoint(C, A)
I == midpoint(B, E)
k == parallel_line(H, f)
J == projection(G, k)

Need to prove:
concyclic(D, F, I, J)

Proof:
