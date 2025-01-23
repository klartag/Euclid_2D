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
k == Line(C, F)
G == line_intersection(i, j)
H == midpoint(G, C)
I == midpoint(B, A)
l == Line(I, H)
J == line_intersection(g, l)
c == Circle(G, J, C)
K in l, c
m == parallel_line(K, h)

Need to prove:
concurrent(j, k, m)

Proof:
