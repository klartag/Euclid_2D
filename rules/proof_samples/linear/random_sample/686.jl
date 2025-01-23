Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M, N: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M, N)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
J == midpoint(B, C)
K == midpoint(B, A)
L == midpoint(G, K)
M == midpoint(G, H)
c == Circle(I, G, J)
N == center(c)

Need to prove:
concyclic(G, L, M, N)

Proof:
