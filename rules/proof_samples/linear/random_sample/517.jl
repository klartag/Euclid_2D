Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(A, g)
j == Line(E, A)
c == Circle(A, B, D)
F in j, c
G == midpoint(F, C)
H == projection(G, j)

Need to prove:
concyclic(A, B, G, H)

Proof:
