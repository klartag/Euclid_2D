Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
d == Circle(C, D, G)
H in h, d
I in d, c
J in j, d
K == projection(I, j)
k == Line(K, I)
L in k, c

Need to prove:
concyclic(F, H, J, L)

Proof:
