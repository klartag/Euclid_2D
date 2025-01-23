Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(D, C)
F == line_intersection(g, i)
G == center(c)
H == midpoint(E, F)
j == Line(E, F)
I in j
J == midpoint(G, I)

Need to prove:
collinear(H, E, J)

Proof:
