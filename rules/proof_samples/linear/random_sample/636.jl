Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l, m)
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
H == projection(D, k)
l == Line(D, H)
I in l
I in m # (defining m)
J == projection(G, m)

Need to prove:
concyclic(G, H, I, J)

Proof:
