Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(C, f)
c == Circle(C, A, E)
d == Circle(A, B, D)
F == midpoint(B, C)
G == center(c)
H == projection(F, i)
j == Line(H, F)
e == Circle(F, G, B)
I == center(d)
J in j, e

Need to prove:
collinear(J, I, G)

Proof:
