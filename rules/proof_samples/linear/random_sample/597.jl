Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l, m: Line
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
H == midpoint(G, B)
I == midpoint(C, A)
J == projection(I, k)
l == Line(J, I)
m == external_angle_bisector(G, F, H)
K == line_intersection(l, m)

Need to prove:
concyclic(C, D, F, K)

Proof:
