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
A in i # (defining i)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(G, C)
I == midpoint(B, C)
J == midpoint(C, A)
c == Circle(C, A, I)
d == Circle(G, J, B)
e == Circle(I, D, F)
K in c, e
L in e, d

Need to prove:
concyclic(F, H, K, L)

Proof:
