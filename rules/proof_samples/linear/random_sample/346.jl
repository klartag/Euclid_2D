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
c == Circle(C, A, B)
D in h, c
i == parallel_line(D, g)
E == line_intersection(f, i)
d == Circle(E, A, C)
F in d
G == midpoint(F, C)
H == midpoint(B, D)

Need to prove:
concyclic(C, D, G, H)

Proof:
