Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E in h, c
d == Circle(D, C, A)
F in g, d
G == midpoint(D, C)
H == midpoint(F, D)
I == midpoint(B, C)

Need to prove:
concyclic(E, G, H, I)

Proof:
