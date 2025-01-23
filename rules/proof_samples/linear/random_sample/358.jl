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
c == Circle(A, B, D)
E == projection(C, i)
F == midpoint(D, C)
G == center(c)
H == midpoint(B, D)
I == projection(G, i)

Need to prove:
concyclic(E, F, H, I)

Proof:
