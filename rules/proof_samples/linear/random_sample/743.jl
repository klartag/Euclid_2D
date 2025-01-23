Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l, m, n, p: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l, m, n, p)
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
D in k # (defining k)
H == line_intersection(g, k)
l == parallel_line(C, f)
I == midpoint(A, H)
m == parallel_line(I, l)
J == projection(E, k)
n == Line(J, E)
K in n, c
p == Line(K, G)

Need to prove:
concurrent(j, m, p)

Proof:
