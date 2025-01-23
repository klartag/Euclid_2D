Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == projection(C, h)
i == Line(C, E)
F == line_intersection(i, f)
G == midpoint(B, F)
H == projection(G, g)
I == center(c)

Need to prove:
concyclic(B, D, H, I)

Proof:
