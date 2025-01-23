Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E in h, c
F == projection(C, f)
j == external_angle_bisector(D, F, B)
G == line_intersection(i, j)
H == midpoint(E, C)
k == external_angle_bisector(A, H, E)
I == line_intersection(i, k)

Need to prove:
concyclic(F, G, H, I)

Proof:
