Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(A, g)
i == external_angle_bisector(A, B, C)
c == Circle(C, A, B)
D in i, c
E in h, c
F == center(c)
G == midpoint(D, E)
d == Circle(G, E, A)
H in f, d
I == projection(E, g)
j == Line(I, E)
J == projection(F, i)
k == Line(F, J)
K == line_intersection(k, j)

Need to prove:
concyclic(B, H, J, K)

Proof:
