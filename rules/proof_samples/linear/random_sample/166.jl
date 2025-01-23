Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, A, B)
E in h, c
F == midpoint(B, A)
G == center(c)
H == midpoint(G, E)
I == midpoint(G, D)

Need to prove:
concyclic(A, F, H, I)

Proof:
