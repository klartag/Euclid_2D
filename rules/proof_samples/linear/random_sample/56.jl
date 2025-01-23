Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
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
c == Circle(B, D, G)
d == Circle(E, D, G)
H == midpoint(F, D)
k == Line(F, D)
I == line_intersection(k, h)
J == center(c)
e == Circle(J, E, I)
K in e, d

Need to prove:
concyclic(F, G, H, K)

Proof:
