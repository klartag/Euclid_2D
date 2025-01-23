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
E == projection(A, g)
F == midpoint(B, A)
c == Circle(F, C, E)
j == Line(B, D)
G == midpoint(C, A)
d == Circle(D, C, A)
H in c, d
I in j, d

Need to prove:
concyclic(F, G, H, I)

Proof:
