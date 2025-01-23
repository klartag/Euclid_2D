Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
d == Circle(B, C, D)
h == external_angle_bisector(A, D, C)
E == midpoint(D, B)
F == center(c)
i == Line(A, F)
G in h, d
H == projection(G, i)

Need to prove:
concyclic(D, E, G, H)

Proof:
