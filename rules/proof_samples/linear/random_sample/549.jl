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
E == projection(A, g)
c == Circle(E, A, D)
F == midpoint(C, A)
G == projection(F, g)
H == center(c)
I == midpoint(B, A)

Need to prove:
concyclic(E, G, H, I)

Proof:
