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
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
d == Circle(E, B, D)
e == Circle(E, D, C)
F == midpoint(E, A)
G in f, d
H == center(e)

Need to prove:
concyclic(D, F, G, H)

Proof:
