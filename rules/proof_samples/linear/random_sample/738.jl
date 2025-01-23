Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
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
H == midpoint(G, C)
c == Circle(H, F, D)
I in i, c
I in k # (defining k)
J == midpoint(A, E)
K == projection(C, k)

Need to prove:
concyclic(D, I, J, K)

Proof:
