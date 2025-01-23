Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(A, B, C)
k == external_angle_bisector(C, D, A)
c == Circle(C, D, B)
E in i, c
F == midpoint(A, E)
G == line_intersection(j, h)
H == projection(C, k)

Need to prove:
concyclic(D, F, G, H)

Proof:
