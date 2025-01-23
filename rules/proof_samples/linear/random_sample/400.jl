Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l, m, n: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l, m, n)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, f)
G == projection(A, k)
l == Line(G, A)
m == Line(F, D)
H == line_intersection(h, m)
n == Line(H, E)

Need to prove:
concurrent(j, l, n)

Proof:
