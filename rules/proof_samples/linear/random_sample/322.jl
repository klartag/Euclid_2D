Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
c == Circle(C, A, B)
D == midpoint(B, C)
E == projection(A, f)
g == Line(E, A)
F == center(c)
h == parallel_line(F, f)
G == line_intersection(g, h)

Need to prove:
concyclic(D, E, F, G)

Proof:
