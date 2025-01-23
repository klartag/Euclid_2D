Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == external_angle_bisector(A, B, C)
k == external_angle_bisector(C, D, B)
E in k, c
F == projection(E, j)
l == Line(E, F)
G in l, c
H == center(c)
m == Line(H, G)

Need to prove:
concurrent(g, i, m)

Proof:
