Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i)
distinct(c, d)
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
c == Circle(G, E, I)
K in c
d == Circle(K, J, D)

Need to prove:
H in d

Proof:
