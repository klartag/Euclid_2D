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
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(A, D)
F == line_intersection(g, i)
d == Circle(C, F, A)
j == parallel_line(E, h)
G == line_intersection(g, j)
H in f, d
I == projection(H, i)

Need to prove:
concyclic(F, G, H, I)

Proof:
