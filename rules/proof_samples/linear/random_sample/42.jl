Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l, m, n: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l, m, n)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
E in l # (defining l)
H == line_intersection(l, k)
m == Line(F, D)
c == Circle(A, G, F)
I == projection(H, i)
n == Line(H, I)
J == line_intersection(m, n)
K in l, c

Need to prove:
collinear(G, K, J)

Proof:
