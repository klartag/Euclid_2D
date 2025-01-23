Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
g == parallel_line(C, f)
E == midpoint(D, A)
h == Line(D, A)
F == midpoint(D, B)
i == Line(D, B)
G == line_intersection(g, i)
H == line_intersection(h, g)

Need to prove:
concyclic(E, F, G, H)

Proof:
