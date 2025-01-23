Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
j == Line(C, A)
E == midpoint(B, D)
F in j, c
G == projection(A, h)
H == center(c)
d == Circle(H, F, E)
I in c, d

Need to prove:
concyclic(D, E, G, I)

Proof:
