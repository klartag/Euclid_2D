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
d == Circle(A, E, B)
F == center(d)
G == center(c)
e == Circle(G, E, D)
H == center(e)

Need to prove:
concyclic(B, F, G, H)

Proof:
