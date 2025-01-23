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
E == projection(B, h)
F == midpoint(B, D)
c == Circle(E, A, D)
G in f, c
j == external_angle_bisector(C, F, G)
H == line_intersection(j, i)
I == center(c)

Need to prove:
concyclic(D, G, H, I)

Proof:
