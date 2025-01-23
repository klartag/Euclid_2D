Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l, m: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l, m)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
j == external_angle_bisector(D, C, E)
F in j, c
k == external_angle_bisector(F, E, B)
d == Circle(F, D, E)
G in i, d
H == projection(G, j)
l == Line(H, G)
m == parallel_line(F, g)

Need to prove:
concurrent(k, l, m)

Proof:
