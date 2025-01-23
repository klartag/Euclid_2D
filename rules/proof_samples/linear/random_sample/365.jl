Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(D, B, A)
E in h, c
i == parallel_line(E, g)
j == parallel_line(D, h)
F == projection(B, j)
G in i, c
H == midpoint(C, A)

Need to prove:
concyclic(A, F, G, H)

Proof:
