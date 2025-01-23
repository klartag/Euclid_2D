Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
E in j # (defining j)
G == line_intersection(i, j)
H == midpoint(B, G)
I == midpoint(G, C)
J == midpoint(C, A)
K == midpoint(B, A)
L in Line(J, I)
k == Line(L, K)
c == Circle(J, H, F)
M in k, c

Need to prove:
false() # concyclic(F, H, I, M)

Proof:
