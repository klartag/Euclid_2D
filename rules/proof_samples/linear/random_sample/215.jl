Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, C)
I == midpoint(B, C)
j == Line(G, H)
c == Circle(G, E, B)
J in j, c
K == midpoint(B, J)

Need to prove:
collinear(K, B, I)

Proof:
