Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
E in f
F in f, c
G == projection(E, g)
H == midpoint(E, B)

Need to prove:
concyclic(C, F, G, H)

Proof:
