Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H, I)
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
k == internal_angle_bisector(D, A, B)
l == internal_angle_bisector(D, C, G)
H == line_intersection(j, l)
I == line_intersection(k, l)

Need to prove:
concyclic(F, G, H, I)

Proof:
