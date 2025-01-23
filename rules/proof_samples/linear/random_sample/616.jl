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
h == internal_angle_bisector(C, A, D)
E == center(c)
F in h, c
G == projection(E, h)
H == midpoint(F, B)

Need to prove:
concyclic(C, D, G, H)

Proof:
