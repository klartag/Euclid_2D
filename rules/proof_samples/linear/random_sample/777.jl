Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
c == Circle(D, C, E)
G == center(c)
j == parallel_line(G, g)
H == midpoint(E, C)
I == line_intersection(i, j)

Need to prove:
concyclic(F, G, H, I)

Proof:
