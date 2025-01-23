Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(A, h)
c == Circle(C, D, B)
d == Circle(E, A, D)
e == Circle(C, A, E)
F in c, e
G == midpoint(D, F)
H == center(d)

Need to prove:
concyclic(A, F, G, H)

Proof:
