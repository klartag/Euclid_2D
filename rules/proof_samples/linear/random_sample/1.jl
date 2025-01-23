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
c == Circle(C, A, B)
E in h, c
j == external_angle_bisector(C, D, A)
F == projection(A, h)
k == Line(A, F)
G == line_intersection(k, j)
H == line_intersection(j, f)

Need to prove:
concyclic(A, E, G, H)

Proof:
