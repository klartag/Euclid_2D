Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(C, f)
F == midpoint(C, E)
G == midpoint(E, F)
H == midpoint(C, G)
I == midpoint(B, D)
c == Circle(G, A, E)
J == center(c)

Need to prove:
concyclic(E, H, I, J)

Proof:
