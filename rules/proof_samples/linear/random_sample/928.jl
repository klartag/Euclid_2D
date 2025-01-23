Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
j == internal_angle_bisector(A, E, B)
d == Circle(E, D, C)
F == center(c)
G in j
H == center(d)
I == midpoint(H, G)
J == midpoint(B, A)
K == midpoint(J, I)

Need to prove:
collinear(F, J, K)

Proof:
