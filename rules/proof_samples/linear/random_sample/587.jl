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
j == external_angle_bisector(A, E, B)
c == Circle(E, A, D)
F in j, c
G == midpoint(B, C)
H == projection(D, f)
I == projection(F, i)

Need to prove:
concyclic(B, G, H, I)

Proof:
