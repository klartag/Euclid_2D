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
E == midpoint(B, C)
F == projection(C, f)
c == Circle(E, A, F)
G == center(c)
H == midpoint(B, D)
I == midpoint(E, A)

Need to prove:
concyclic(E, G, H, I)

Proof:
