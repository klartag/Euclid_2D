Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == projection(D, f)
h == internal_angle_bisector(A, C, B)
F == midpoint(E, C)
G in h, c
H == projection(E, h)

Need to prove:
concyclic(D, F, G, H)

Proof:
