Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
j == parallel_line(I, i)
J == midpoint(G, H)
c == Circle(J, H, E)
K == center(c)
d == Circle(I, J, E)
L in j, d

Need to prove:
collinear(J, K, L)

Proof:
