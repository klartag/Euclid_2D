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
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
k == external_angle_bisector(F, G, B)
l == external_angle_bisector(C, A, F)
c == Circle(D, C, A)
H == line_intersection(k, l)
d == Circle(H, E, G)
e == Circle(A, B, E)
I == center(d)
J == center(e)
K == center(c)

Need to prove:
concyclic(F, I, J, K)

Proof:
