Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(A, D)
F == projection(A, h)
c == Circle(F, B, C)
G == midpoint(F, C)
H == center(c)

Need to prove:
concyclic(E, F, G, H)

Proof:
