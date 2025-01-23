Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l)
distinct(c, d, e)
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
l == external_angle_bisector(F, E, G)
H in l, c
I == line_intersection(l, k)
J == line_intersection(l, f)
d == Circle(D, A, G)
e == Circle(E, D, H)
K in e, d

Need to prove:
concyclic(D, I, J, K)

Proof:
