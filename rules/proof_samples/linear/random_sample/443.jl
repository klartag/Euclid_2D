Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(G, E, A)
H == projection(D, h)
k == Line(D, H)
I == center(c)
l == Line(E, F)
J == projection(C, l)
m == Line(C, J)
K == line_intersection(k, m)

Need to prove:
collinear(K, E, I)

Proof:
