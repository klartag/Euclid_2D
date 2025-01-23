Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
H == midpoint(B, G)
I == midpoint(H, B)
k == internal_angle_bisector(G, F, E)
l == internal_angle_bisector(I, G, E)

Need to prove:
concurrent(j, k, l)

Proof:
