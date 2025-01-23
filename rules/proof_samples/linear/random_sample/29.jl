Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(C, i)
c == Circle(C, B, E)
F == projection(A, g)
d == Circle(D, E, C)
G == center(d)
H == midpoint(C, F)
I == center(c)

Need to prove:
concyclic(C, G, H, I)

Proof:
