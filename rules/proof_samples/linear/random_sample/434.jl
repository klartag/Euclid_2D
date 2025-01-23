Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
E == midpoint(C, D)
d == Circle(D, B, A)
F == center(d)
g == Line(F, D)
G == line_intersection(g, f)

Need to prove:
concyclic(C, E, F, G)

Proof:
