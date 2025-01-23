Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L, M: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L, M)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, B)
H == midpoint(F, C)
I == midpoint(B, C)
J == midpoint(C, A)
K == midpoint(B, A)
c == Circle(E, J, I)
d == Circle(L, J, A)
M in c, d

Need to prove:
concyclic(G, H, K, M)

Proof:
