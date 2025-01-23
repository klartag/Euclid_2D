Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(B, D)
c == Circle(A, B, D)
k == external_angle_bisector(D, B, C)
E == line_intersection(k, h)
F == projection(C, k)
l == Line(F, C)
G in h, c
H == line_intersection(l, j)

Need to prove:
concyclic(B, E, G, H)

Proof:
