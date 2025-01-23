Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
D == projection(A, h)
c == Circle(D, C, A)
E == midpoint(B, A)
i == parallel_line(E, g)
F in g, c
G == line_intersection(i, h)

Need to prove:
concyclic(C, E, F, G)

Proof:
