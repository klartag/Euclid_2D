Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(B, A)
d == Circle(E, B, C)
e == Circle(D, A, E)
j == Line(B, D)
F in e, d
k == parallel_line(F, j)
G == center(c)
H == line_intersection(g, i)
l == Line(D, G)
I == line_intersection(k, l)

Need to prove:
concyclic(C, D, H, I)

Proof:
