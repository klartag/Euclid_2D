Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
k == Line(E, F)
G == line_intersection(k, j)
H == projection(E, f)
l == Line(H, E)
I == line_intersection(l, j)

Need to prove:
concyclic(B, G, H, I)

Proof:
