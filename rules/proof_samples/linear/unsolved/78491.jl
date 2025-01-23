Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(F, E, G)
d == Circle(E, B, G)
l == external_angle_bisector(B, F, C)
H in l, c
I in k, d
J == line_intersection(l, i)
K == projection(J, f)

Need to prove:
concyclic(G, H, I, K)

Proof:
