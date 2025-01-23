Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(C, A)
h == internal_angle_bisector(E, D, B)
d == Circle(A, E, D)
F in h, c
G in f, d
H == projection(G, h)

Need to prove:
concyclic(A, E, F, H)

Proof:
