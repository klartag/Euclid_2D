Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(B, C)
I == midpoint(B, A)
J == midpoint(G, H)
K == midpoint(I, E)
L == midpoint(D, E)

Need to prove:
concyclic(E, J, K, L)

Proof:
