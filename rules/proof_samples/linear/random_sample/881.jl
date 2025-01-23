Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(D, f)
c == Circle(C, A, B)
d == Circle(D, E, B)
F in c, d
G == projection(A, h)
H == midpoint(F, D)

Need to prove:
concyclic(D, E, G, H)

Proof:
