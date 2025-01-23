Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(B, C)
F == midpoint(A, D)
d == Circle(B, E, F)
G == line_intersection(g, i)
j == Line(D, E)
k == Line(C, F)
H == line_intersection(k, j)
I == center(d)
J == projection(H, h)

Need to prove:
collinear(J, I, G)

Proof:
