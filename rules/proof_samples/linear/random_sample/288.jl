Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(C, A, D)
E in h, c
F == projection(D, h)
i == Line(F, D)
E in j # (defining j)
G == midpoint(B, A)
H == line_intersection(i, f)
I == projection(H, j)

Need to prove:
concyclic(F, G, H, I)

Proof:
