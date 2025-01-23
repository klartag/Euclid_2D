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
E == midpoint(D, C)
F == midpoint(B, C)
G == midpoint(A, D)
H == projection(E, f)
c == Circle(E, H, B)
I in h, c

Need to prove:
concyclic(D, F, G, I)

Proof:
