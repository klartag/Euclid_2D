Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == midpoint(B, A)
j == Line(E, F)
G == center(c)
H == line_intersection(j, h)
I == projection(G, g)

Need to prove:
concyclic(C, G, H, I)

Proof:
