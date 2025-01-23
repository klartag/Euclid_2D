Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
c == Circle(C, B, E)
F == midpoint(E, A)
G == center(c)
G in j # (defining j)
H == projection(F, j)
I == midpoint(C, E)

Need to prove:
concyclic(F, G, H, I)

Proof:
