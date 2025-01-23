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
E == midpoint(B, D)
F == midpoint(E, A)
G == midpoint(F, A)
c == Circle(F, E, B)
H in f, c

Need to prove:
concyclic(B, C, G, H)

Proof:
