Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
distinct(c, d, e)
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
d == Circle(F, B, C)
H in d, c
e == Circle(F, I, H)
J == center(d)
K == midpoint(J, D)
L == center(e)

Need to prove:
collinear(L, J, K)

Proof:
