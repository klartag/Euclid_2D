Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
G == midpoint(C, D)
c == Circle(G, F, E)
H in g, c
I == projection(H, j)
d == Circle(E, I, D)
J == center(d)
K == midpoint(H, E)

Need to prove:
concyclic(E, G, J, K)

Proof:
