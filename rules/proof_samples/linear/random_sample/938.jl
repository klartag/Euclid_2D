Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(E, D, B)
H == midpoint(F, A)
I == center(c)
J == midpoint(A, E)
K == midpoint(D, A)
d == Circle(K, I, H)
e == Circle(J, G, K)
L in d, e

Need to prove:
concyclic(C, E, I, L)

Proof:
