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
E == midpoint(D, B)
F == midpoint(D, C)
G == center(c)
H == midpoint(C, E)
i == Line(H, F)
I == line_intersection(h, i)

Need to prove:
concyclic(A, F, G, I)

Proof:
