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
c == Circle(C, A, B)
E in h
F == midpoint(D, E)
G == projection(E, i)
H in h, c

Need to prove:
concyclic(A, F, G, H)

Proof:
