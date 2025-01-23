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
E == projection(C, f)
F == midpoint(D, C)
c == Circle(C, A, E)
G == midpoint(B, A)
H in i, c

Need to prove:
concyclic(A, F, G, H)

Proof:
