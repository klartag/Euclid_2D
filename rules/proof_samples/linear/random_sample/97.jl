Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(B, G)
I == midpoint(C, A)
k == parallel_line(A, j)
l == external_angle_bisector(F, H, D)
J == line_intersection(l, k)

Need to prove:
concyclic(A, H, I, J)

Proof:
