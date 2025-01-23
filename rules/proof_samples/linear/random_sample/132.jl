Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
D == midpoint(B, C)
E == midpoint(B, A)
F == midpoint(D, A)
f == Line(D, A)
g == Line(F, B)
h == parallel_line(D, g)
i == parallel_line(C, f)
G == line_intersection(h, i)
j == Line(F, E)
c == Circle(D, C, G)
H in j, c

Need to prove:
concyclic(B, C, F, H)

Proof:
