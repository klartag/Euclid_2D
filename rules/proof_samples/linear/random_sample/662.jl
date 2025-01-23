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
c == Circle(C, D, B)
E in f, c
d == Circle(E, A, C)
F in h, d
G == projection(E, h)
H == projection(F, i)

Need to prove:
concyclic(A, C, G, H)

Proof:
