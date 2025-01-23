Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
j == external_angle_bisector(E, B, D)
F == center(c)
G in j, c
d == Circle(G, E, D)
H == center(d)
I == midpoint(C, H)
J in g, d
K == midpoint(B, H)
e == Circle(G, K, I)
L in d, e

Need to prove:
collinear(J, F, L)

Proof:
