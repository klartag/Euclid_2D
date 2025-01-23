Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == projection(C, h)
i == Line(C, E)
F in i, c
j == parallel_line(F, h)
G == line_intersection(f, j)
H == midpoint(G, F)
d == Circle(E, F, H)
I in d, c

Need to prove:
collinear(H, I, B)

Proof:
