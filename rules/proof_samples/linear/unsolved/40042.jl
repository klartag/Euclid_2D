Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
k == Line(F, G)
l == external_angle_bisector(G, E, F)
H in k
m == external_angle_bisector(A, G, H)

Need to prove:
concurrent(i, l, m)

Proof:
