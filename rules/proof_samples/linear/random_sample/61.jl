Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l, m, n: Line
c: Circle
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
c == Circle(G, F, E)
k == external_angle_bisector(A, G, D)
H == projection(E, f)
l == Line(H, E)
I in k, c
m == parallel_line(G, l)
n == parallel_line(I, f)

Need to prove:
concurrent(i, m, n)

Proof:
