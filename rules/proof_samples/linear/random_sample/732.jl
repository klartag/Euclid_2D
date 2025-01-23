Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(B, C)
D == projection(A, f)
E == midpoint(C, A)
c == Circle(B, C, E)
d == Circle(C, D, A)
F == center(c)
g == Line(F, E)
G in d, c
H == line_intersection(g, f)

Need to prove:
concyclic(B, F, G, H)

Proof:
