Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == projection(C, f)
j == Line(E, C)
F == projection(D, f)
G == line_intersection(i, j)
H == projection(E, g)

Need to prove:
concyclic(E, F, G, H)

Proof:
