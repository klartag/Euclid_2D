Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == parallel_line(C, f)
D == midpoint(C, A)
E == midpoint(B, A)
F == midpoint(E, B)
h == Line(D, F)
G == line_intersection(g, h)
c == Circle(F, A, G)
H in g, c

Need to prove:
concyclic(B, C, E, H)

Proof:
