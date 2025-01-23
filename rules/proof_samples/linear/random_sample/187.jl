Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
A in c
B in c
C in c
D in c
f == Line(D, B)
E == midpoint(C, A)
g == Line(E, B)
h == parallel_line(C, g)
F == midpoint(A, D)
G == line_intersection(h, f)
i == Line(F, E)
H == line_intersection(i, f)

Need to prove:
concyclic(A, C, G, H)

Proof:
