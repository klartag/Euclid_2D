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
i == parallel_line(D, g)
E in i, c
F == center(c)
j == Line(C, F)
G == projection(A, j)
H == projection(E, g)

Need to prove:
concyclic(C, E, G, H)

Proof:
