Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
i == Line(E, B)
d == Circle(A, E, B)
F in h, d
G == projection(C, i)
j == Line(G, C)
H in j, c

Need to prove:
collinear(H, B, F)

Proof:
