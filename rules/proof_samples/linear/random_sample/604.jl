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
i == Line(D, A)
j == Line(B, E)
F == line_intersection(i, j)
G == midpoint(A, F)
H == midpoint(C, F)
I == projection(G, h)
k == Line(I, G)
l == internal_angle_bisector(E, H, D)

Need to prove:
concurrent(f, k, l)

Proof:
