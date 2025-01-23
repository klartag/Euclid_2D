Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l, m, n: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l, m, n)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
k == Line(G, C)
H == midpoint(B, A)
I == midpoint(A, F)
l == Line(I, H)
m == Line(E, A)
n == parallel_line(B, l)

Need to prove:
concurrent(k, m, n)

Proof:
