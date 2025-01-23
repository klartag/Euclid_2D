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
c == Circle(C, A, G)
H == center(c)
k == Line(F, D)
I == projection(H, k)
l == Line(I, H)
m == parallel_line(H, f)
J == line_intersection(j, m)
K == projection(C, l)

Need to prove:
concyclic(E, H, J, K)

Proof:
