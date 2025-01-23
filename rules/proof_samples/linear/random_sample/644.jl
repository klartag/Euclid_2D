Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
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
H == line_intersection(h, j)
d == Circle(D, F, H)
I == projection(C, j)
J in c, d
k == Line(C, J)
K in k, c

Need to prove:
concyclic(C, G, I, K)

Proof:
