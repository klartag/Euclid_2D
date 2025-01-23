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
E == projection(A, h)
c == Circle(A, E, B)
F == midpoint(D, E)
G == center(c)
H == midpoint(C, A)
I == projection(F, f)

Need to prove:
concyclic(B, G, H, I)

Proof:
