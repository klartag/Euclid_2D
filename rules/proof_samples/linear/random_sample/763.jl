Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(F, D)
k == Line(F, D)
I == projection(F, h)
l == Line(I, F)
c == Circle(I, H, C)
J in k, c
K in l, c

Need to prove:
collinear(K, G, J)

Proof:
